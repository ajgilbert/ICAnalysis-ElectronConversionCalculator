import FWCore.ParameterSet.Config as cms

icElectronConversionCalculator = cms.EDProducer('ICElectronConversionCalculator',
    input       = cms.InputTag("gsfElectrons"),
    beamspot    = cms.InputTag("offlineBeamSpot"),
    conversions = cms.InputTag("allConversions")
)

icElectronConversionFromMiniAODCalculator = cms.EDProducer('ICElectronConversionFromMiniAODCalculator',
    input       = cms.InputTag("slimmedElectrons"),
    beamspot    = cms.InputTag("offlineBeamSpot"),
    conversions = cms.InputTag("reducedEgamma:reducedConversions")
)


icElectronConversionFromPatCalculator = cms.EDProducer('ICElectronConversionFromPatCalculator',
    input       = cms.InputTag("patElectrons")
)
