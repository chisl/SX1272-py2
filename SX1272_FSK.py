#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""SX1272: 860 MHz to 1020 MHz Low Power Long Range Transceiver featuring the LoRa (TM) long range modem"""

__author__     = "ChISL"
__copyright__  = "TBD"
__credits__    = ["Semtech"]
__license__    = "TBD"
__version__    = "0.1"
__maintainer__ = "https://chisl.io"
__email__      = "info@chisl.io"
__status__     = "Test"

from SX1272_constants import *

# name:        SX1272
# description: 860 MHz to 1020 MHz Low Power Long Range Transceiver featuring the LoRa (TM) long range modem
# manuf:       Semtech
# version:     0.1
# url:         http://www.semtech.com/images/datasheet/sx1272.pdf
# date:        2016-08-01


# Derive from this class and implement read and write
class SX1272_Base:
	"""860 MHz to 1020 MHz Low Power Long Range Transceiver featuring the LoRa (TM) long range modem"""
	# Register Fifo
	# FIFO data input/output 
	
	def setFifo(self, val):
		"""Set register Fifo"""
		self.write(REG.Fifo, val, 8)
	
	def getFifo(self):
		"""Get register Fifo"""
		return self.read(REG.Fifo, 8)
	
	# Bits Fifo
	# Register OpMode
	
	
	def setOpMode(self, val):
		"""Set register OpMode"""
		self.write(REG.OpMode, val, 8)
	
	def getOpMode(self):
		"""Get register OpMode"""
		return self.read(REG.OpMode, 8)
	
	# Bits LongRangeMode
	# This bit can be modified only in Sleep mode. 
	#           A write operation on other device modes is ignored. 
	
	# Bits ModulationType
	# Modulation scheme: 
	# 'b10, 'b11: reserved 
	
	# Bits ModulationShaping
	# Data shaping: 
	#           In FSK:
	#           - 00: no shaping
	#           - 01: Gaussian filter BT = 1.0 10 
	#           - 10: Gaussian filter BT = 0.5 11 
	#           - 11: Gaussian filter BT = 0.3 
	#           In OOK:
	#           - 00: no shaping
	#           - 01: filtering with fcutoff = bit_rate10
	#           - 10: filtering with fcutoff = 2*bit_rate (for bit_rate < 125 kbps) 
	#           - 11: reserved 
	
	# Bits Mode
	# Transceiver modes 
	# Register BitrateMsb
	# MSB of Bit Rate (chip rate if Manchester encoding is enabled) 
	
	def setBitrateMsb(self, val):
		"""Set register BitrateMsb"""
		self.write(REG.BitrateMsb, val, 8)
	
	def getBitrateMsb(self):
		"""Get register BitrateMsb"""
		return self.read(REG.BitrateMsb, 8)
	
	# Bits BitrateMsb
	# Register BitrateLsb
	# LSB of bit rate (chip rate if Manchester encoding is enabled)BitRate =  ---------------------------F----X----O-----S---C------------------------------BitRate(15,0) + -B----i--t--r--a----t--e---F----r--a----c-16Default value: 4.8 kbps 
	
	def setBitrateLsb(self, val):
		"""Set register BitrateLsb"""
		self.write(REG.BitrateLsb, val, 8)
	
	def getBitrateLsb(self):
		"""Get register BitrateLsb"""
		return self.read(REG.BitrateLsb, 8)
	
	# Bits BitrateLsb
	# Register FdevMsb
	
	
	def setFdevMsb(self, val):
		"""Set register FdevMsb"""
		self.write(REG.FdevMsb, val, 8)
	
	def getFdevMsb(self):
		"""Get register FdevMsb"""
		return self.read(REG.FdevMsb, 8)
	
	# Bits unused_0
	# unused 
	# Bits Fdev
	# MSB of the frequency deviation 
	# Register FdevLsb
	# LSB of the frequency deviationFdev = Fstep  Fdev(15,0)Default value: 5 kHz 
	
	def setFdevLsb(self, val):
		"""Set register FdevLsb"""
		self.write(REG.FdevLsb, val, 8)
	
	def getFdevLsb(self):
		"""Get register FdevLsb"""
		return self.read(REG.FdevLsb, 8)
	
	# Bits FdevLsb
	# Register FrfMsb
	# MSB of the RF carrier frequency 
	
	def setFrfMsb(self, val):
		"""Set register FrfMsb"""
		self.write(REG.FrfMsb, val, 8)
	
	def getFrfMsb(self):
		"""Get register FrfMsb"""
		return self.read(REG.FrfMsb, 8)
	
	# Bits FrfMsb
	# Register FrfMid
	# MSB of the RF carrier frequency 
	
	def setFrfMid(self, val):
		"""Set register FrfMid"""
		self.write(REG.FrfMid, val, 8)
	
	def getFrfMid(self):
		"""Get register FrfMid"""
		return self.read(REG.FrfMid, 8)
	
	# Bits FrfMid
	# Register FrfLsb
	# LSB of RF carrier frequencyFrf = Fstep  Frf23;0Default value: 915.000 MHzThe RF frequency is taken into account internally only when:entering FSRX/FSTX modesre-starting the receiver 
	
	def setFrfLsb(self, val):
		"""Set register FrfLsb"""
		self.write(REG.FrfLsb, val, 8)
	
	def getFrfLsb(self):
		"""Get register FrfLsb"""
		return self.read(REG.FrfLsb, 8)
	
	# Bits FrfLsb
	# Register PaConfig
	
	
	def setPaConfig(self, val):
		"""Set register PaConfig"""
		self.write(REG.PaConfig, val, 8)
	
	def getPaConfig(self):
		"""Get register PaConfig"""
		return self.read(REG.PaConfig, 8)
	
	# Bits PaSelect
	# Selects PA output pin0  RFO pin. Maximum power of +13 dBm1  PA_BOOST pin. Maximum power of +20 dBm 
	# Bits unused_0
	# unused 
	# Bits OutputPower
	# Output power setting, with 1dB stepsPout = 2 + OutputPower [dBm], on PA_BOOST pin Pout = -1 + OutputPower [dBm], on RFO pin 
	# Register PaRamp
	
	
	def setPaRamp(self, val):
		"""Set register PaRamp"""
		self.write(REG.PaRamp, val, 8)
	
	def getPaRamp(self):
		"""Get register PaRamp"""
		return self.read(REG.PaRamp, 8)
	
	# Bits unused_0
	# unused 
	# Bits LowPnTxPllOff
	# Select a higher power, lower phase noise PLL only when the transmitter is used:
	#           0 : Standard PLL used in Rx mode, Lower PN PLL in Tx
	#           1 : Standard PLL used in both Tx and Rx modes 
	
	# Bits PaRamp
	# Rise/Fall time of ramp up/down in FSK 
	# Register Ocp
	
	
	def setOcp(self, val):
		"""Set register Ocp"""
		self.write(REG.Ocp, val, 8)
	
	def getOcp(self):
		"""Get register Ocp"""
		return self.read(REG.Ocp, 8)
	
	# Bits unused_0
	# unused 
	# Bits OcpOn
	# Enables overload current protection (OCP) for the PA: 0  OCP disabled1  OCP enabled 
	# Bits OcpTrim
	# Trimming of OCP current:Imax = 45+5*OcpTrim [mA] if OcpTrim <= 15 (120 mA) /Imax = -30+10*OcpTrim [mA] if 15 < OcpTrim <= 27 (130 to 240 mA)Imax = 240mA for higher settings Default Imax = 100mA 
	# Register Lna
	
	
	def setLna(self, val):
		"""Set register Lna"""
		self.write(REG.Lna, val, 8)
	
	def getLna(self):
		"""Get register Lna"""
		return self.read(REG.Lna, 8)
	
	# Bits LnaGain
	# LNA gain setting: 000  reserved001  G1 = highest gain010  G2 = highest gain – 6 dB 011  G3 = highest gain – 12 dB 100  G4 = highest gain – 24 dB 101  G5 = highest gain – 36 dB 110  G6 = highest gain – 48 dB 111  reservedNote:Reading this address always returns the current LNA gain (which may be different from what had been previously selected if AGC is enabled. 
	# Bits unused_0
	# Bits LnaBoost
	# Improves the system Noise Figure at the expense of Rx current consumption:00  Default setting, meeting the specification 11  Improved sensitivity 
	# Register RxConfig
	
	
	def setRxConfig(self, val):
		"""Set register RxConfig"""
		self.write(REG.RxConfig, val, 8)
	
	def getRxConfig(self):
		"""Get register RxConfig"""
		return self.read(REG.RxConfig, 8)
	
	# Bits RestartRxOnCollision
	# Turns on the mechanism restarting the receiver automatically if it gets saturated or a packet collision is detected0  No automatic Restart 1  Automatic restart On 
	# Bits RestartRxWithoutPllLock
	# Triggers a manual Restart of the Receiver chain when set to 1. Use this bit when there is no frequency change, RestartRxWithPllLock otherwise. 
	# Bits RestartRxWithPllLock
	# Triggers a manual Restart of the Receiver chain when set to 1. Use this bit when there is a frequency change, requiring some time for the PLL to re-lock. 
	# Bits AfcAutoOn
	# 0  No AFC performed at receiver startup1  AFC is performed at each receiver startup 
	# Bits AgcAutoOn
	# 0  LNA gain forced by the LnaGain Setting 1  LNA gain is controlled by the AGC 
	# Bits RxTrigger
	# Selects the event triggering AGC and/or AFC at receiver startup. See Table Table 23 for a description. 
	# Register RssiConfig
	
	
	def setRssiConfig(self, val):
		"""Set register RssiConfig"""
		self.write(REG.RssiConfig, val, 8)
	
	def getRssiConfig(self):
		"""Get register RssiConfig"""
		return self.read(REG.RssiConfig, 8)
	
	# Bits RssiOffset
	# Signed RSSI offset, to compensate for the possible losses/gains in the front-end (LNA, SAW filter...)1dB / LSB, 2’s complement format 
	# Bits RssiSmoothing
	# Defines the number of samples taken to average the RSSI result: 000  2 samples used001  4 samples used 8 samples used 16 samples used 32 samples used 64 samples used 128 samples used 256 samples used 
	# Register RssiCollision
	# Sets the threshold used to consider that an interferer is detected, witnessing a packet collision. 1dB/LSB (only RSSI increase) Default: 10dB 
	
	def setRssiCollision(self, val):
		"""Set register RssiCollision"""
		self.write(REG.RssiCollision, val, 8)
	
	def getRssiCollision(self):
		"""Get register RssiCollision"""
		return self.read(REG.RssiCollision, 8)
	
	# Bits RssiCollision
	# Register RssiThresh
	# RSSI trigger level for the Rssi interrupt:- RssiThreshold / 2 [dBm] 
	
	def setRssiThresh(self, val):
		"""Set register RssiThresh"""
		self.write(REG.RssiThresh, val, 8)
	
	def getRssiThresh(self):
		"""Get register RssiThresh"""
		return self.read(REG.RssiThresh, 8)
	
	# Bits RssiThresh
	# Register RssiValue
	# Absolute value of the RSSI in dBm, 0.5dB steps. RSSI = - RssiValue/2 [dBm] 
	
	def setRssiValue(self, val):
		"""Set register RssiValue"""
		self.write(REG.RssiValue, val, 8)
	
	def getRssiValue(self):
		"""Get register RssiValue"""
		return self.read(REG.RssiValue, 8)
	
	# Bits RssiValue
	# Register RxBw
	
	
	def setRxBw(self, val):
		"""Set register RxBw"""
		self.write(REG.RxBw, val, 8)
	
	def getRxBw(self):
		"""Get register RxBw"""
		return self.read(REG.RxBw, 8)
	
	# Bits unused_0
	# unused 
	# Bits reserved_1
	# reserved 
	# Bits RxBwMant
	# Channel filter bandwidth control: RxBwMant = 16            10  RxBwMant = 24 RxBwMant = 20            11  reserved 
	# Bits RxBwExp
	# Channel filter bandwidth control: FSK Mode:RxBw = ------------------------F----X----O----S----C--------------------------RxBwMant  2RxBwExp + 2 
	# Register AfcBw
	
	
	def setAfcBw(self, val):
		"""Set register AfcBw"""
		self.write(REG.AfcBw, val, 8)
	
	def getAfcBw(self):
		"""Get register AfcBw"""
		return self.read(REG.AfcBw, 8)
	
	# Bits reserved_0
	# reserved 
	# Bits RxBwMantAfc
	# RxBwMant parameter used during the AFC 
	# Bits RxBwExpAfc
	# RxBwExp parameter used during the AFC 
	# Register OokPeak
	
	
	def setOokPeak(self, val):
		"""Set register OokPeak"""
		self.write(REG.OokPeak, val, 8)
	
	def getOokPeak(self):
		"""Get register OokPeak"""
		return self.read(REG.OokPeak, 8)
	
	# Bits reserved_0
	# reserved 
	# Bits BitSyncOn
	# Enables the Bit Synchronizer.0  Bit Sync disabled (not possible in Packet mode) 1  Bit Sync enabled 
	# Bits OokThreshType
	# Selects the type of threshold in the OOK data slicer: 00  fixed threshold             10  average mode 01  peak mode (default)       11  reserved 
	# Bits OokPeakTheshStep
	# Size of each decrement of the RSSI threshold in the OOK demodulator:000  0.5 dB           001  1.0 dB010  1.5 dB           011  2.0 dB100  3.0 dB           101  4.0 dB110  5.0 dB          111  6.0 dB 
	# Register OokFix
	# Fixed threshold for the Data Slicer in OOK modeFloor threshold for the Data Slicer in OOK when Peak mode is used 
	
	def setOokFix(self, val):
		"""Set register OokFix"""
		self.write(REG.OokFix, val, 8)
	
	def getOokFix(self):
		"""Get register OokFix"""
		return self.read(REG.OokFix, 8)
	
	# Bits OokFix
	# Register OokAvg
	
	
	def setOokAvg(self, val):
		"""Set register OokAvg"""
		self.write(REG.OokAvg, val, 8)
	
	def getOokAvg(self):
		"""Get register OokAvg"""
		return self.read(REG.OokAvg, 8)
	
	# Bits OokPeakThreshDec
	# Period of decrement of the RSSI threshold in the OOK demodulator:000  once per chip             001  once every 2 chips 010  once every 4 chips     011  once every 8 chips 100  twice in each chip      101  4 times in each chip 110  8 times in each chip   111  16 times in each chip 
	# Bits reserved_0
	# reserved 
	# Bits OokAverageOffset
	# Static offset added to the threshold in average mode in order to reduce glitching activity (OOK only):00  0.0 dB                         10  4.0 dB01  2.0 dB                         11  6.0 dB 
	# Bits OokAverageThreshFilt
	# Filter coefficients in average mode of the OOK demodulator: 00  fC ≈ chip rate / 32.π      01  fC ≈ chip rate / 8.π10  fC ≈ chip rate / 4.π        11 fC ≈ chip rate / 2.π 
	# Register AfcFei
	
	
	def setAfcFei(self, val):
		"""Set register AfcFei"""
		self.write(REG.AfcFei, val, 8)
	
	def getAfcFei(self):
		"""Get register AfcFei"""
		return self.read(REG.AfcFei, 8)
	
	# Bits unused_0
	# unused 
	# Bits AgcStart
	# Triggers an AGC sequence when set to 1. 
	# Bits reserved_1
	# reserved 
	# Bits unused_2
	# unused 
	# Bits AfcClear
	# Clear AFC register set in Rx mode. Always reads 0. 
	# Bits AfcAutoClearOn
	# Only valid if AfcAutoOn is set0  AFC register is not cleared at the beginning of the automatic AFC phase1  AFC register is cleared at the beginning of the automatic AFC phase 
	# Register AfcMsb
	# MSB of the AfcValue, 2’s complement format. Can be used to overwrite the current AFC value 
	
	def setAfcMsb(self, val):
		"""Set register AfcMsb"""
		self.write(REG.AfcMsb, val, 8)
	
	def getAfcMsb(self):
		"""Get register AfcMsb"""
		return self.read(REG.AfcMsb, 8)
	
	# Bits AfcMsb
	# Register AfcLsb
	# LSB of the AfcValue, 2’s complement format. Can be used to overwrite the current AFC value 
	
	def setAfcLsb(self, val):
		"""Set register AfcLsb"""
		self.write(REG.AfcLsb, val, 8)
	
	def getAfcLsb(self):
		"""Get register AfcLsb"""
		return self.read(REG.AfcLsb, 8)
	
	# Bits AfcLsb
	# Register Fei
	# measured frequency offset, 2’s complement. Frequency error = FeiValue x Fstep 
	
	def setFei(self, val):
		"""Set register Fei"""
		self.write(REG.Fei, val, 16)
	
	def getFei(self):
		"""Get register Fei"""
		return self.read(REG.Fei, 16)
	
	# Bits Fei
	# Register PreambleDetect
	
	
	def setPreambleDetect(self, val):
		"""Set register PreambleDetect"""
		self.write(REG.PreambleDetect, val, 8)
	
	def getPreambleDetect(self):
		"""Get register PreambleDetect"""
		return self.read(REG.PreambleDetect, 8)
	
	# Bits PreambleDetectorOn
	# Enables Preamble detector when set to 1. The AGC settings supersede this bit during the startup / AGC phase.0  Turned off 1  Turned on 
	# Bits PreambleDetectorSize
	# Number of Preamble bytes to detect to trigger an interrupt 00  1 byte                            10  3 bytes01  2 bytes                           11  Reserved 
	# Bits PreambleDetectorTol
	# Number or chip errors tolerated over PreambleDetectorSize. 4 chips per bit. 
	# Register RxTimeout1
	# Timeout interrupt is generated TimeoutRxRssi*16*Tbit after switching to Rx mode if Rssi interrupt doesn’t occur (i.e.RssiValue > RssiThreshold)0x00: TimeoutRxRssi is disabled 
	
	def setRxTimeout1(self, val):
		"""Set register RxTimeout1"""
		self.write(REG.RxTimeout1, val, 8)
	
	def getRxTimeout1(self):
		"""Get register RxTimeout1"""
		return self.read(REG.RxTimeout1, 8)
	
	# Bits RxTimeout1
	# Register RxTimeout2
	# Timeout interrupt is generated TimeoutRxPreamble*16*Tbit after switching to Rx mode if Preamble interrupt doesn’t occur0x00: TimeoutRxPreamble is disabled 
	
	def setRxTimeout2(self, val):
		"""Set register RxTimeout2"""
		self.write(REG.RxTimeout2, val, 8)
	
	def getRxTimeout2(self):
		"""Get register RxTimeout2"""
		return self.read(REG.RxTimeout2, 8)
	
	# Bits RxTimeout2
	# Register RxTimeout3
	# Timeout interrupt is generated TimeoutSignalSync*16*Tbit after the Rx mode is programmed, if SyncAddress doesn’t occur 0x00: TimeoutSignalSync is disabled 
	
	def setRxTimeout3(self, val):
		"""Set register RxTimeout3"""
		self.write(REG.RxTimeout3, val, 8)
	
	def getRxTimeout3(self):
		"""Get register RxTimeout3"""
		return self.read(REG.RxTimeout3, 8)
	
	# Bits RxTimeout3
	# Register RxDelay
	# Additional delay before an automatic receiver restart is launched: Delay = InterPacketRxDelay*4*Tbit 
	
	def setRxDelay(self, val):
		"""Set register RxDelay"""
		self.write(REG.RxDelay, val, 8)
	
	def getRxDelay(self):
		"""Get register RxDelay"""
		return self.read(REG.RxDelay, 8)
	
	# Bits RxDelay
	# Register Osc
	
	
	def setOsc(self, val):
		"""Set register Osc"""
		self.write(REG.Osc, val, 8)
	
	def getOsc(self):
		"""Get register Osc"""
		return self.read(REG.Osc, 8)
	
	# Bits unused_0
	# Bits RcCalStart
	# Triggers the calibration of the RC oscillator when set. Always reads 0. RC calibration must be triggered in Standby mode. 
	# Bits ClkOut
	# Selects CLKOUT frequency: 000  FXOSC001  FXOSC / 2 FXOSC / 4 FXOSC / 8 FXOSC / 16 FXOSC / 32110  RC (automatically enabled) 111  OFF 
	# Register PreambleMsb
	# Size of the preamble to be sent (from TxStartCondition fulfilled). (MSB byte) 
	
	def setPreambleMsb(self, val):
		"""Set register PreambleMsb"""
		self.write(REG.PreambleMsb, val, 8)
	
	def getPreambleMsb(self):
		"""Get register PreambleMsb"""
		return self.read(REG.PreambleMsb, 8)
	
	# Bits PreambleMsb
	# Register PreambleLsb
	# Size of the preamble to be sent (from TxStartCondition fulfilled). (LSB byte) 
	
	def setPreambleLsb(self, val):
		"""Set register PreambleLsb"""
		self.write(REG.PreambleLsb, val, 8)
	
	def getPreambleLsb(self):
		"""Get register PreambleLsb"""
		return self.read(REG.PreambleLsb, 8)
	
	# Bits PreambleLsb
	# Register SyncConfig
	
	
	def setSyncConfig(self, val):
		"""Set register SyncConfig"""
		self.write(REG.SyncConfig, val, 8)
	
	def getSyncConfig(self):
		"""Get register SyncConfig"""
		return self.read(REG.SyncConfig, 8)
	
	# Bits AutoRestartRxMode
	# Controls the automatic restart of the receiver after the reception of a valid packet (PayloadReady or CrcOk): Off On, without waiting for the PLL to re-lock10  On, wait for the PLL to lock (frequency changed) 11  reserved 
	# Bits PreamblePolarity
	# Sets the polarity of the Preamble 0  0xAA (default)1  0x55 
	# Bits SyncOn
	# Enables the Sync word generation and detection: 0  Off1  On 
	# Bits FifoFillCondition
	# FIFO filling condition:0  if SyncAddress interrupt occurs  1  as long as FifoFillCondition is set 
	# Bits SyncSize
	# Size of the Sync word:(SyncSize + 1) bytes, (SyncSize) bytes if ioHomeOn=1 
	# Register SyncValue1
	# 1st byte of Sync word. (MSB byte) Used if SyncOn is set. 
	
	def setSyncValue1(self, val):
		"""Set register SyncValue1"""
		self.write(REG.SyncValue1, val, 8)
	
	def getSyncValue1(self):
		"""Get register SyncValue1"""
		return self.read(REG.SyncValue1, 8)
	
	# Bits SyncValue1
	# Register SyncValue2
	# 2nd byte of Sync wordUsed if SyncOn is set and (SyncSize +1) >= 2. 
	
	def setSyncValue2(self, val):
		"""Set register SyncValue2"""
		self.write(REG.SyncValue2, val, 8)
	
	def getSyncValue2(self):
		"""Get register SyncValue2"""
		return self.read(REG.SyncValue2, 8)
	
	# Bits SyncValue2
	# Register SyncValue3
	# 3rd byte of Sync word.Used if SyncOn is set and (SyncSize +1) >= 3. 
	
	def setSyncValue3(self, val):
		"""Set register SyncValue3"""
		self.write(REG.SyncValue3, val, 8)
	
	def getSyncValue3(self):
		"""Get register SyncValue3"""
		return self.read(REG.SyncValue3, 8)
	
	# Bits SyncValue3
	# Register SyncValue4
	# 4th byte of Sync word.Used if SyncOn is set and (SyncSize +1) >= 4. 
	
	def setSyncValue4(self, val):
		"""Set register SyncValue4"""
		self.write(REG.SyncValue4, val, 8)
	
	def getSyncValue4(self):
		"""Get register SyncValue4"""
		return self.read(REG.SyncValue4, 8)
	
	# Bits SyncValue4
	# Register SyncValue5
	# 5th byte of Sync word.Used if SyncOn is set and (SyncSize +1) >= 5. 
	
	def setSyncValue5(self, val):
		"""Set register SyncValue5"""
		self.write(REG.SyncValue5, val, 8)
	
	def getSyncValue5(self):
		"""Get register SyncValue5"""
		return self.read(REG.SyncValue5, 8)
	
	# Bits SyncValue5
	# Register SyncValue6
	# 6th byte of Sync word.Used if SyncOn is set and (SyncSize +1) >= 6. 
	
	def setSyncValue6(self, val):
		"""Set register SyncValue6"""
		self.write(REG.SyncValue6, val, 8)
	
	def getSyncValue6(self):
		"""Get register SyncValue6"""
		return self.read(REG.SyncValue6, 8)
	
	# Bits SyncValue6
	# Register SyncValue7
	# 7th byte of Sync word.Used if SyncOn is set and (SyncSize +1) >= 7. 
	
	def setSyncValue7(self, val):
		"""Set register SyncValue7"""
		self.write(REG.SyncValue7, val, 8)
	
	def getSyncValue7(self):
		"""Get register SyncValue7"""
		return self.read(REG.SyncValue7, 8)
	
	# Bits SyncValue7
	# Register SyncValue8
	# 8th byte of Sync word.Used if SyncOn is set and (SyncSize +1) = 8. 
	
	def setSyncValue8(self, val):
		"""Set register SyncValue8"""
		self.write(REG.SyncValue8, val, 8)
	
	def getSyncValue8(self):
		"""Get register SyncValue8"""
		return self.read(REG.SyncValue8, 8)
	
	# Bits SyncValue8
	# Register PacketConfig1
	
	
	def setPacketConfig1(self, val):
		"""Set register PacketConfig1"""
		self.write(REG.PacketConfig1, val, 8)
	
	def getPacketConfig1(self):
		"""Get register PacketConfig1"""
		return self.read(REG.PacketConfig1, 8)
	
	# Bits PacketFormat
	# Defines the packet format used: 0  Fixed length1  Variable length 
	# Bits DcFree
	# Defines DC-free encoding/decoding performed: 00  None (Off)01  Manchester Whitening reserved 
	# Bits CrcOn
	# Enables CRC calculation/check (Tx/Rx): 0  Off1  On 
	# Bits CrcAutoClearOff
	# Defines the behavior of the packet handler when CRC check fails: 0  Clear FIFO and restart new packet reception. No PayloadReady interrupt issued.1  Do not clear FIFO. PayloadReady interrupt issued. 
	# Bits AddressFiltering
	# Defines address based filtering in Rx: 00  None (Off)01  Address field must match NodeAddress 10  Address field must match NodeAddress or BroadcastAddress11  reserved 
	# Bits CrcWhiteningType
	# Selects the CRC and whitening algorithms:0  CCITT CRC implementation with standard whitening 1  IBM CRC implementation with alternate whitening 
	# Register PacketConfig2
	
	
	def setPacketConfig2(self, val):
		"""Set register PacketConfig2"""
		self.write(REG.PacketConfig2, val, 8)
	
	def getPacketConfig2(self):
		"""Get register PacketConfig2"""
		return self.read(REG.PacketConfig2, 8)
	
	# Bits unused_0
	# unused 
	# Bits DataMode
	# Data processing mode: 
	# Bits IoHomeOn
	# Enables the io-homecontrol® compatibility mode 0  Disabled1  Enabled 
	# Bits IoHomePowerFrame
	# reserved - Linked to io-homecontrol® compatibility mode 
	# Bits BeaconOn
	# Enables the Beacon mode in Fixed packet format 
	# Bits PayloadLength
	# Packet Length Most significant bits 
	# Register PayloadLength
	# If PacketFormat = 0 (fixed), payload length.If PacketFormat = 1 (variable), max length in Rx, not used in Tx. 
	
	def setPayloadLength(self, val):
		"""Set register PayloadLength"""
		self.write(REG.PayloadLength, val, 8)
	
	def getPayloadLength(self):
		"""Get register PayloadLength"""
		return self.read(REG.PayloadLength, 8)
	
	# Bits PayloadLength
	# Register NodeAdrs
	# Node address used in address filtering. 
	
	def setNodeAdrs(self, val):
		"""Set register NodeAdrs"""
		self.write(REG.NodeAdrs, val, 8)
	
	def getNodeAdrs(self):
		"""Get register NodeAdrs"""
		return self.read(REG.NodeAdrs, 8)
	
	# Bits NodeAdrs
	# Register BroadcastAdrs
	# Broadcast address used in address filtering. 
	
	def setBroadcastAdrs(self, val):
		"""Set register BroadcastAdrs"""
		self.write(REG.BroadcastAdrs, val, 8)
	
	def getBroadcastAdrs(self):
		"""Get register BroadcastAdrs"""
		return self.read(REG.BroadcastAdrs, 8)
	
	# Bits BroadcastAdrs
	# Register FifoThresh
	
	
	def setFifoThresh(self, val):
		"""Set register FifoThresh"""
		self.write(REG.FifoThresh, val, 8)
	
	def getFifoThresh(self):
		"""Get register FifoThresh"""
		return self.read(REG.FifoThresh, 8)
	
	# Bits TxStartCondition
	# Defines the condition to start packet transmission:0  FifoLevel (i.e. the number of bytes in the FIFO exceedsFifoThreshold)1  FifoEmpty goes low(i.e. at least one byte in the FIFO) 
	# Bits unused_0
	# unused 
	# Bits FifoThreshold
	# Used to trigger FifoLevel interrupt, when: number of bytes in FIFO >= FifoThreshold + 1 
	# Register SeqConfig1
	
	
	def setSeqConfig1(self, val):
		"""Set register SeqConfig1"""
		self.write(REG.SeqConfig1, val, 8)
	
	def getSeqConfig1(self):
		"""Get register SeqConfig1"""
		return self.read(REG.SeqConfig1, 8)
	
	# Bits SequencerStart
	# Controls the top level SequencerWhen set to ‘1’, executes the “Start” transition.The sequencer can only be enabled when the chip is in Sleep or Standby mode. 
	# Bits SequencerStop
	# Forces the Sequencer Off. Always reads ‘0’ 
	# Bits IdleMode
	# Selects chip mode during the state: 0: Standby mode1: Sleep mode 
	# Bits FromStart
	# Controls the Sequencer transition when SequencerStart is set to 1 in Sleep or Standby mode:00: to LowPowerSelection 01: to Receive state10: to Transmit state11: to Transmit state on a FifoLevel interrupt 
	# Bits LowPowerSelection
	# Selects the Sequencer LowPower state after a to LowPowerSelection transition:0: SequencerOff state with chip on Initial mode1: Idle state with chip on Standby or Sleep mode depending onIdleModeNote:   Initial mode is the chip LowPower mode at Sequencer Start. 
	# Bits FromIdle
	# Controls the Sequencer transition from the Idle state on a T1 interrupt:0: to Transmit state 1: to Receive state 
	# Bits FromTransmit
	# Controls the Sequencer transition from the Transmit state: 0: to LowPowerSelection on a PacketSent interrupt1: to Receive state on a PacketSent interrupt 
	# Register SeqConfig2
	
	
	def setSeqConfig2(self, val):
		"""Set register SeqConfig2"""
		self.write(REG.SeqConfig2, val, 8)
	
	def getSeqConfig2(self):
		"""Get register SeqConfig2"""
		return self.read(REG.SeqConfig2, 8)
	
	# Bits FromReceive
	# Controls the Sequencer transition from the Receive state 000 and 111: unused001: to PacketReceived state on a PayloadReady interrupt 010: to LowPowerSelection on a PayloadReady interrupt 011: to PacketReceived state on a CrcOk interrupt (1)100: to SequencerOff state on a Rssi interrupt101: to SequencerOff state on a SyncAddress interrupt 110: to SequencerOff state on a PreambleDetect interruptIrrespective of this setting, transition to LowPowerSelection on a T2 interrupt(1) If the CRC is wrong (corrupted packet, with CRC on but CrcAutoClearOn=0), the PayloadReady interrupt will drive the sequencer to RxTimeout state. 
	# Bits FromRxTimeout
	# Controls the state-machine transition from the Receive state on a RxTimeout interrupt (and on PayloadReady if FromReceive = 011):00: to Receive State, via ReceiveRestart 01: to Transmit state10: to LowPowerSelection 11: to SequencerOff stateNote:   RxTimeout interrupt is a TimeoutRxRssi, TimeoutRxPreamble or TimeoutSignalSync interrupt 
	# Bits FromPacketReceived
	# Controls the state-machine transition from the PacketReceived state:000: to SequencerOff state001: to Transmit state on a FifoEmpty interrupt 010: to LowPowerSelection011: to Receive via FS mode, if frequency was changed 100: to Receive state (no frequency change) 
	# Register TimerResol
	
	
	def setTimerResol(self, val):
		"""Set register TimerResol"""
		self.write(REG.TimerResol, val, 8)
	
	def getTimerResol(self):
		"""Get register TimerResol"""
		return self.read(REG.TimerResol, 8)
	
	# Bits unused_0
	# unused 
	# Bits Timer1Resolution
	# Resolution of Timer 1 00: Timer1 disabled01: 64 us10: 4.1 ms11: 262 ms 
	# Bits Timer2Resolution
	# Resolution of Timer 2 00: Timer2 disabled01: 64 us10: 4.1 ms11: 262 ms 
	# Register Timer1Coef
	# Multiplying coefficient for Timer 1 
	
	def setTimer1Coef(self, val):
		"""Set register Timer1Coef"""
		self.write(REG.Timer1Coef, val, 8)
	
	def getTimer1Coef(self):
		"""Get register Timer1Coef"""
		return self.read(REG.Timer1Coef, 8)
	
	# Bits Timer1Coef
	# Register Timer2Coef
	# Multiplying coefficient for Timer 2 
	
	def setTimer2Coef(self, val):
		"""Set register Timer2Coef"""
		self.write(REG.Timer2Coef, val, 8)
	
	def getTimer2Coef(self):
		"""Get register Timer2Coef"""
		return self.read(REG.Timer2Coef, 8)
	
	# Bits Timer2Coef
	# Register ImageCal
	
	
	def setImageCal(self, val):
		"""Set register ImageCal"""
		self.write(REG.ImageCal, val, 8)
	
	def getImageCal(self):
		"""Get register ImageCal"""
		return self.read(REG.ImageCal, 8)
	
	# Bits AutoImageCalOn
	# Controls the Image calibration mechanism0  Calibration of the receiver depending on the temperature is disabled1  Calibration of the receiver depending on the temperature enabled. 
	# Bits ImageCalStart
	# Triggers the IQ and RSSI calibration when set in Standby mode. 
	# Bits ImageCalRunning
	# Set to 1 while the Image and RSSI calibration are running. Toggles back to 0 when the process is completed 
	# Bits unused_0
	# unused 
	# Bits TempChange
	# IRQ flag witnessing a temperature change exceeding TempThreshold since the last Image and RSSI calibration: 0  Temperature change lower than TempThreshold1  Temperature change greater than TempThreshold 
	# Bits TempThreshold
	# Temperature change threshold to trigger a new I/Q calibration 00  5 °C01  10 °C10  15 °C11  20 °C 
	# Bits TempMonitorOff
	# Controls the temperature monitor operation:0  Temperature monitoring done in all modes except Sleep and Standby1  Temperature monitoring stopped. 
	# Register Temp
	# Measured temperature-1°C per LsbNeeds calibration for absolute accuracy 
	
	def setTemp(self, val):
		"""Set register Temp"""
		self.write(REG.Temp, val, 8)
	
	def getTemp(self):
		"""Get register Temp"""
		return self.read(REG.Temp, 8)
	
	# Bits Temp
	# Register LowBat
	
	
	def setLowBat(self, val):
		"""Set register LowBat"""
		self.write(REG.LowBat, val, 8)
	
	def getLowBat(self):
		"""Get register LowBat"""
		return self.read(REG.LowBat, 8)
	
	# Bits unused_0
	# unused 
	# Bits LowBatOn
	# Low Battery detector enable signal 0  LowBat detector disabled1  LowBat detector enabled 
	# Bits LowBatTrim
	# Trimming of the LowBat threshold: 000  1.695 V001  1.764 V010  1.835 V (d)011  1.905 V100  1.976 V101  2.045 V110  2.116 V111  2.185 V 
	# Register IrqFlags1
	
	
	def setIrqFlags1(self, val):
		"""Set register IrqFlags1"""
		self.write(REG.IrqFlags1, val, 8)
	
	def getIrqFlags1(self):
		"""Get register IrqFlags1"""
		return self.read(REG.IrqFlags1, 8)
	
	# Bits ModeReady
	# Set when the operation mode requested in Mode, is readySleep: Entering Sleep modeStandby: XO is runningFS: PLL is lockedRx: RSSI sampling startsTx: PA ramp-up completedCleared when changing the operating mode. 
	# Bits RxReady
	# Set in Rx mode, after RSSI, AGC and AFC. Cleared when leaving Rx. 
	# Bits TxReady
	# Set in Tx mode, after PA ramp-up. Cleared when leaving Tx. 
	# Bits PllLock
	# Set (in FS, Rx or Tx) when the PLL is locked. Cleared when it is not. 
	# Bits Rssi
	# Set in Rx when the RssiValue exceeds RssiThreshold.Cleared when leaving Rx or setting this bit to 1. 
	# Bits Timeout
	# Set when a timeout occursCleared when leaving Rx or FIFO is emptied. 
	# Bits PreambleDetect
	# Set when the Preamble Detector has found valid Preamble. bit clear when set to 1 
	# Bits SyncAddressMatch
	# Set when Sync and Address (if enabled) are detected. Cleared when leaving Rx or FIFO is emptied.This bit is read only in Packet mode, rwc in Continuous mode 
	# Register IrqFlags2
	
	
	def setIrqFlags2(self, val):
		"""Set register IrqFlags2"""
		self.write(REG.IrqFlags2, val, 8)
	
	def getIrqFlags2(self):
		"""Get register IrqFlags2"""
		return self.read(REG.IrqFlags2, 8)
	
	# Bits FifoFull
	# Set when FIFO is full (i.e. contains 66 bytes), else cleared. 
	# Bits FifoEmpty
	# Set when FIFO is empty, and cleared when there is at least 1 byte in the FIFO. 
	# Bits FifoLevel
	# Set when the number of bytes in the FIFO strictly exceedsFifoThreshold, else cleared. 
	# Bits FifoOverrun
	# Set when FIFO overrun occurs. (except in Sleep mode)Flag(s) and FIFO are cleared when this bit is set. The FIFO then becomes immediately available for the next transmission / reception. 
	# Bits PacketSent
	# Set in Tx when the complete packet has been sent. Cleared when exiting Tx 
	# Bits PayloadReady
	# Set in Rx when the payload is ready (i.e. last byte received and CRC, if enabled and CrcAutoClearOff is cleared, is Ok). Cleared when FIFO is empty. 
	# Bits CrcOk
	# Set in Rx when the CRC of the payload is Ok. Cleared when FIFO is empty. 
	# Bits LowBat
	# Set when the battery voltage drops below the Low Battery threshold. Cleared only when set to 1 by the user. 
	# Register DioMapping1
	
	
	def setDioMapping1(self, val):
		"""Set register DioMapping1"""
		self.write(REG.DioMapping1, val, 8)
	
	def getDioMapping1(self):
		"""Get register DioMapping1"""
		return self.read(REG.DioMapping1, 8)
	
	# Bits Dio0Mapping
	# Mapping of pins DIO0 to DIO5See Table 17 for mapping in LoRa modeSee Table 28 for mapping in Continuous mode.
	#           See Table 29 for mapping in Packet mode 
	
	# Bits Dio1Mapping
	# None 
	# Bits Dio2Mapping
	# None 
	# Bits Dio3Mapping
	# Register DioMapping2
	
	
	def setDioMapping2(self, val):
		"""Set register DioMapping2"""
		self.write(REG.DioMapping2, val, 8)
	
	def getDioMapping2(self):
		"""Get register DioMapping2"""
		return self.read(REG.DioMapping2, 8)
	
	# Bits Dio4Mapping
	# Bits Dio5Mapping
	# Bits reserved_0
	# Bits MapPreambleDetect
	# Allows the mapping of either Rssi Or PreambleDetect to the DIO pins, as summarized on 
	#           Table 28 and Table 29 
	
	# Register Version
	# Version code of the chip. Bits 7-4 give the full revision number; bits 3-0 give the metal mask revision number. 
	
	def setVersion(self, val):
		"""Set register Version"""
		self.write(REG.Version, val, 8)
	
	def getVersion(self):
		"""Get register Version"""
		return self.read(REG.Version, 8)
	
	# Bits Version
	# Register AgcRef
	
	
	def setAgcRef(self, val):
		"""Set register AgcRef"""
		self.write(REG.AgcRef, val, 8)
	
	def getAgcRef(self):
		"""Get register AgcRef"""
		return self.read(REG.AgcRef, 8)
	
	# Bits unused_0
	# unused 
	# Bits AgcReferenceLevel
	# Sets the floor reference for all AGC thresholds: AGC Reference [dBm] =-174 dBm + 10*log(2*RxBw) + SNR + AgcReferenceLevelSNR = 8 dB, fixed value 
	# Register AgcThresh1
	
	
	def setAgcThresh1(self, val):
		"""Set register AgcThresh1"""
		self.write(REG.AgcThresh1, val, 8)
	
	def getAgcThresh1(self):
		"""Get register AgcThresh1"""
		return self.read(REG.AgcThresh1, 8)
	
	# Bits unused_0
	# unused 
	# Bits AgcStep1
	# Defines the 1st AGC Threshold 
	# Register AgcThresh2
	
	
	def setAgcThresh2(self, val):
		"""Set register AgcThresh2"""
		self.write(REG.AgcThresh2, val, 8)
	
	def getAgcThresh2(self):
		"""Get register AgcThresh2"""
		return self.read(REG.AgcThresh2, 8)
	
	# Bits AgcStep2
	# Defines the 2nd AGC Threshold: 
	# Bits AgcStep3
	# Defines the 3rd AGC Threshold: 
	# Register AgcThresh3
	
	
	def setAgcThresh3(self, val):
		"""Set register AgcThresh3"""
		self.write(REG.AgcThresh3, val, 8)
	
	def getAgcThresh3(self):
		"""Get register AgcThresh3"""
		return self.read(REG.AgcThresh3, 8)
	
	# Bits AgcStep4
	# Defines the 4th AGC Threshold: 
	# Bits AgcStep5
	# Defines the 5th AGC Threshold: 
	# Register PllHop
	
	
	def setPllHop(self, val):
		"""Set register PllHop"""
		self.write(REG.PllHop, val, 8)
	
	def getPllHop(self):
		"""Get register PllHop"""
		return self.read(REG.PllHop, 8)
	
	# Bits FastHopOn
	# Bypasses the main state machine for a quick frequency hop. Writing RegFrfLsb will trigger the frequency change.0  Frf is validated when FSTx or FSRx is requested1  Frf is validated triggered when RegFrfLsb is written 
	# Bits reserved_0
	# reserved 
	# Register Tcxo
	
	
	def setTcxo(self, val):
		"""Set register Tcxo"""
		self.write(REG.Tcxo, val, 8)
	
	def getTcxo(self):
		"""Get register Tcxo"""
		return self.read(REG.Tcxo, 8)
	
	# Bits reserved_0
	# reserved. Retain default value 
	# Bits TcxoInputOn
	# Controls the crystal oscillator0  Crystal Oscillator with external Crystal1  External clipped sine TCXO AC-connected to XTA pin 
	# Bits reserved_1
	# Reserved. Retain default value. 
	# Register PaDac
	
	
	def setPaDac(self, val):
		"""Set register PaDac"""
		self.write(REG.PaDac, val, 8)
	
	def getPaDac(self):
		"""Get register PaDac"""
		return self.read(REG.PaDac, 8)
	
	# Bits reserved_0
	# reserved. Retain default value 
	# Bits PaDac
	# Enables the +20 dBm option on PA_BOOST pin 0x04  Default value0x07  +20 dBm on PA_BOOST when OutputPower = 1111 
	# Register Pll
	
	
	def setPll(self, val):
		"""Set register Pll"""
		self.write(REG.Pll, val, 8)
	
	def getPll(self):
		"""Get register Pll"""
		return self.read(REG.Pll, 8)
	
	# Bits PllBandwidth
	# Controls the PLL bandwidth:00  75 kHz                          10  225 kHz01  150 kHz                        11  300 kHz 
	# Bits reserved_0
	# reserved. Retain default value 
	# Register PllLowPn
	
	
	def setPllLowPn(self, val):
		"""Set register PllLowPn"""
		self.write(REG.PllLowPn, val, 8)
	
	def getPllLowPn(self):
		"""Get register PllLowPn"""
		return self.read(REG.PllLowPn, 8)
	
	# Bits PllBandwidth
	# Controls the Low Phase Noise PLL bandwidth: 00  75 kHz                          10  225 kHz01  150 kHz                        11  300 kHz 
	# Bits reserved_0
	# reserved. Retain default value 
	# Register FormerTemp
	# Temperature saved during the latest IQ (RSSI and Image) calibrated. Same format as TempValue in RegTemp. 
	
	def setFormerTemp(self, val):
		"""Set register FormerTemp"""
		self.write(REG.FormerTemp, val, 8)
	
	def getFormerTemp(self):
		"""Get register FormerTemp"""
		return self.read(REG.FormerTemp, 8)
	
	# Bits FormerTemp
	# Register BitrateFrac
	
	
	def setBitrateFrac(self, val):
		"""Set register BitrateFrac"""
		self.write(REG.BitrateFrac, val, 8)
	
	def getBitrateFrac(self):
		"""Get register BitrateFrac"""
		return self.read(REG.BitrateFrac, 8)
	
	# Bits unused_0
	# unused 
	# Bits BitRateFrac
	# Fractional part of the bit rate divider (Only valid for FSK) If BitRateFrac> 0 then:BitRate =  ---------------------------F----X----O-----S---C------------------------------BitRate(15,0) + -B----i--t--r--a----t--e---F----r--a----c-16 
