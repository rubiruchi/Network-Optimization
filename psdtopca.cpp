// PSD (TI RF Packet Sniffer Format) to PCAP Converter
// Version 1.0.0
// This program takes in a PSD file and converts it to PCAP format for use in programs like Wireshark.
// Copyright (C) 2010 Torrey M. Bievenour

//  This program is free software: you can redistribute it and/or modify
//    it under the terms of the GNU General Public License as published by
//    the Free Software Foundation, either version 3 of the License, or
//    (at your option) any later version.
//  This program is distributed in the hope that it will be useful,
//    but WITHOUT ANY WARRANTY; without even the implied warranty of
//    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
//    GNU General Public License for more details.
//  You should have received a copy of the GNU General Public License
//    along with this program.  If not, see <http://www.gnu.org/licenses/>.


// PSD_2_PCAP_Convert.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>

using namespace std;

const int PSD_Packet_Size = 151;

#pragma pack(show)
#pragma pack(push,1)	// Required to keep memory and file alignment the same for structures

struct PSD_Packet_s
{
	unsigned __int8 Information;
	unsigned __int32 Number;
	unsigned __int64 Timestamp;
	unsigned __int16 aux;
	unsigned __int8 Length;
	unsigned char Remainder[135];	// Based on fixed record size of 151 bytes
};

struct PCAP_Packet_Header_s
{
	unsigned __int32 ts_sec;
	unsigned __int32 ts_usec;
	unsigned __int32 incl_len;
	unsigned __int32 orig_len;
};

#pragma pack(pop)
#pragma pack(show)

unsigned _int64 endian_swap(unsigned __int64 x)
{
	return (x >> 56) |
		((x << 40) & 0x00FF000000000000) |
		((x << 24) & 0x0000FF0000000000) |
		((x << 8) & 0x000000FF00000000) |
		((x >> 8) & 0x00000000FF000000) |
		((x >> 24) & 0x0000000000FF0000) |
		((x >> 40) & 0x000000000000FF00) |
		(x << 56);
}

unsigned _int32 endian_swap(unsigned __int32 x)
{
	return (x >> 24) |
		((x << 8) & 0x00FF0000) |
		((x >> 8) & 0x0000FF00) |
		(x << 24);
}

int _tmain()
{
	string argv[3];
	argv[1] = "C:\\Users\\superuser\\Documents\\suyash ps work\\1106.PSD_2_PCAP_Convert 1.0.0\\DataAnalytics2.psd";
	argv[2] = "C:\\Users\\superuser\\Documents\\suyash ps work\\1106.PSD_2_PCAP_Convert 1.0.0\\analyticsnew2.pcap";
	//cout << "Input File: " << argv[1] << endl;
	//cout << "Output File: " << argv[2] << endl;

	ifstream inFile;
	PSD_Packet_s inPacket;	// Incoming PSD packet
	char * inPacketData;	// Incoming actual packet data
	unsigned __int8 inPacketDataLength;		// Length of incoming actual packet data
	unsigned __int8 FCS1;	// FCS Byte 1 from PSD packet
	unsigned __int8 FCS2;	// FCS Byte 2 from PSD packet
	ofstream outFile;
	int firstPass = 1;		// Track whether output is first pass
	PCAP_Packet_Header_s outPacket;	// Outgoing PCAP packet header
	unsigned __int64 initTimestamp;
	inFile.open(argv[1], ios::in | ios::binary); //  | ios::ate
	if (inFile.is_open())
	{
		while (!inFile.eof())
		{
			inFile.read((char *)(&inPacket), sizeof(inPacket));
			//inPacket.Number = endian_swap(inPacket.Number);
			//inPacket.Timestamp = endian_swap(inPacket.Timestamp);
			if (inPacket.Information & 0x01)		// Check Intformation byte to see if length includes FCS
			{
				inPacketDataLength = inPacket.Length - 2;
			}
			else
			{
				inPacketDataLength = inPacket.Length;
			}
			// Extract packet data
			inPacketData = new char[inPacketDataLength];
			for (int i = 0; i<inPacketDataLength; i++)
			{
				inPacketData[i] = inPacket.Remainder[i];
			}
			// Extract FCS data
			FCS1 = inPacket.Remainder[inPacketDataLength + 0];
			FCS2 = inPacket.Remainder[inPacketDataLength + 1];
			if (inPacket.Number == 1){
				initTimestamp = inPacket.Timestamp;
			}
			float t = (inPacket.Timestamp - initTimestamp) / 32.0;
			float d = t - floor(t);
			if (d >= 0.5)
			{
				inPacket.Timestamp = ceil(t);
			}
			else
			{
				inPacket.Timestamp = floor(t);
			}
			cout << "Packet" << endl;
			cout << inPacket.Information << endl;
			cout << inPacket.Number << endl;
			cout << inPacket.Timestamp << endl;
			cout << inPacket.Length << endl;
			cout << "<STARTREMAIN>" << inPacket.Remainder << "<ENDREMAIN>" << endl;
			cout << "<STARTDATA>" << inPacketData[0] << "<ENDDATA>" << endl;
			cout << "<STARTFCS>" << FCS1 << FCS2 << "<ENDFCS>" << endl;

			if (firstPass == 1)
			{
				outFile.open(argv[2], ios::out | ios::binary | ios::trunc);
				if (outFile.is_open())
				{
					// Write global header
					unsigned __int32 pcapMagicNumber = 0xa1b2c3d4;	// Native byte ordering
					unsigned __int16 pcapVersionMajor = 2;	// Current version is 2.4
					unsigned __int16 pcapVersionMinor = 4;
					signed __int32 pcapThisZone = 0;		// GMT
					unsigned __int32 pcapSigFigs = 0;		// Zero value for sig figs as standard
					unsigned __int32 pcapSnapLen = 128;		// Max Zigbee packet length
					unsigned __int32 pcapNetwork = 0xC3;	// Ethernet = 1, 802 Networks = 6, From Wireshark sample PCAP = 0xC3
					outFile.write((char *)&pcapMagicNumber, sizeof(pcapMagicNumber));
					outFile.write((char *)&pcapVersionMajor, sizeof(pcapVersionMajor));
					outFile.write((char *)&pcapVersionMinor, sizeof(pcapVersionMinor));
					outFile.write((char *)&pcapThisZone, sizeof(pcapThisZone));
					outFile.write((char *)&pcapSigFigs, sizeof(pcapSigFigs));
					outFile.write((char *)&pcapSnapLen, sizeof(pcapSnapLen));
					outFile.write((char *)&pcapNetwork, sizeof(pcapNetwork));
				}
				else cout << "Unable to open output file.";
				firstPass = 0;
			}
			if (outFile.is_open())
			{
				// Write packet header
				outPacket.ts_sec = (long)(inPacket.Timestamp / 1000000);	// Convert to integer seconds
				outPacket.ts_usec = (long)inPacket.Timestamp - (outPacket.ts_sec * 1000000);	// Pick up remainder
				outPacket.incl_len = inPacketDataLength + 2;	// Get data length as included (include FCS)
				outPacket.orig_len = inPacketDataLength + 4;	// Get data length as original (include FCS)
				outFile.write((char *)(&outPacket), sizeof(outPacket));
				// Write packet data
				outFile.write(inPacketData, inPacketDataLength);
				// Write FCS data
				outFile.write((char *)(&FCS1), sizeof(FCS1));
				outFile.write((char *)(&FCS2), sizeof(FCS2));
			}
		}
		inFile.close();
		outFile.close();
	}
	else cout << "Unable to open input file.";

	return 0;
}

