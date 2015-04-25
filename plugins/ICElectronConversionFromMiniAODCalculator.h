#ifndef UserCode_ICHiggsTauTau_ICElectronConversionFromMiniAODCalculator_h
#define UserCode_ICHiggsTauTau_ICElectronConversionFromMiniAODCalculator_h

#include "FWCore/Framework/interface/EDProducer.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/EventSetup.h"
#include "FWCore/Utilities/interface/InputTag.h"

/**
 * @brief Produces an edm::ValueMap<bool> for the electron conversion-rejection
 *flag
 */
class ICElectronConversionFromMiniAODCalculator : public edm::EDProducer {
 public:
  explicit ICElectronConversionFromMiniAODCalculator(const edm::ParameterSet &);
  ~ICElectronConversionFromMiniAODCalculator();

 private:
  virtual void beginJob();
  virtual void produce(edm::Event &, const edm::EventSetup &);
  virtual void endJob();

  edm::InputTag input_;
  edm::InputTag input_beamspot_;
  edm::InputTag input_conversions_;
};

#endif
