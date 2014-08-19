import FWCore.ParameterSet.Config as cms

icElectronConversionCalculator = cms.EDProducer('ICElectronConversionCalculator',
    input       = cms.InputTag("gsfElectrons"),
    beamspot    = cms.InputTag("offlineBeamSpot"),
    conversions = cms.InputTag("allConversions")
)

icElectronConversionFromPatCalculator = cms.EDProducer('ICElectronConversionFromPatCalculator',
    input       = cms.InputTag("patElectrons")
)
