import uproot
import pandas as pd
import time
import numpy as np

import infofile


lumi = 10.0643 # 10 fb-1
fraction = 1
MC_to_data_ratio = 0.033
tuple_path = "/eos/project/a/atlas-outreach/projects/open-data/OpenDataTuples/renamedLargeRJets/exactly2lep/" # local
#tuple_path = "https://atlas-opendata.web.cern.ch/atlas-opendata/samples/2020/2lep/" # web


samples = {

    'data': {
        'list' : ['data_A','data_B','data_C','data_D']
    },

    'ttZ' : {
        'list' : ['ttee','ttmumu'],
    },

    'ttbar' : {
        'list' : ['ttbar_lep'],
    },

    'Z' : {
        'list' : ['Zmumu_PTV500_1000', # Z->μμ + jets, with 500 < pT(Z) < 1000 GeV
                  'Zmumu_PTV1000_E_CMS', # Z->μμ + jets with 1000 GeV < pT(Z) < centre-of-mass energy
                  'Zee_PTV500_1000', # Z->ee + jets with 500 < pT(Z) < 1000 GeV
                  'Zee_PTV1000_E_CMS', # Z->ee + jets with 1000 GeV < pT(Z) < centre-of-mass energy
                  'Zmumu_PTV0_70_BFilter', # Z->μμ + jets with 0 < pT(Z) < 70 GeV and a requirement for b-jets
                  'Zmumu_PTV70_140_BFilter', # Z->μμ + jets with 70 < pT(Z) < 140 GeV and a requirement for b-jets
                  'Zmumu_PTV140_280_BFilter', # Z->μμ + jets with 140 < pT(Z) < 280 GeV and a requirement for b-jets
                  'Zmumu_PTV280_500_BFilter', # Z->μμ + jets with 280 < pT(Z) < 500 GeV and a requirement for b-jets
                  'Zee_PTV0_70_BFilter', # Z->ee + jets with 0 < pT(Z) < 70 GeV and a requirement for b-jets
                  'Zee_PTV70_140_BFilter', # Z->ee + jets with 70 < pT(Z) < 140 GeV and a requirement for b-jets
                  'Zee_PTV140_280_BFilter', # Z->ee + jets with 140 < pT(Z) < 280 GeV and a requirement for b-jets
                  'Zee_PTV280_500_BFilter', # Z->ee + jets with 280 < pT(Z) < 500 GeV and a requirement for b-jets
                  'Zmumu_PTV0_70_CFilterBVeto', # Z->μμ + jets with 0 < pT(Z) < 70 GeV and a requirement for c-jets, whilst vetoing b-jets
                  'Zmumu_PTV70_140_CFilterBVeto', # Z->μμ + jets with 70 < pT(Z) < 140 GeV and a requirement for c-jets, whilst vetoing b-jets
                  'Zmumu_PTV140_280_CFilterBVeto', # Z->μμ + jets with 140 < pT(Z) < 280 GeV and a requirement for c-jets, whilst vetoing b-jets
                  'Zmumu_PTV280_500_CFilterBVeto', # Z->μμ + jets with 280 < pT(Z) < 500 GeV and a requirement for c-jets, whilst vetoing b-jets
                  'Zee_PTV0_70_CFilterBVeto', # Z->ee + jets with 0 < pT(Z) < 70 GeV and a requirement for c-jets, whilst vetoing b-jets
                  'Zee_PTV70_140_CFilterBVeto', # Z->ee + jets with 70 < pT(Z) < 140 GeV and a requirement for c-jets, whilst vetoing b-jets
                  'Zee_PTV140_280_CFilterBVeto', # Z->ee + jets with 140 < pT(Z) < 280 GeV and a requirement for c-jets, whilst vetoing b-jets
                  'Zee_PTV280_500_CFilterBVeto', # Z->ee + jets with 280 < pT(Z) < 500 GeV and a requirement for c-jets, whilst vetoing b-jets
                  'Zmumu_PTV0_70_CVetoBVeto', # Z->μμ + jets with 0 < pT(Z) < 70 GeV whilst vetoing c and b-jets
                  'Zmumu_PTV70_140_CVetoBVeto', # Z->μμ + jets with 70 < pT(Z) < 140 GeV whilst vetoing c and b-jets
                  'Zmumu_PTV140_280_CVetoBVeto', # Z->μμ + jets with 140 < pT(Z) < 280 GeV whilst vetoing c and b-jets
                  'Zmumu_PTV280_500_CVetoBVeto', # Z->μμ + jets with 280 < pT(Z) < 500 GeV whilst vetoing c and b-jets
                  'Zee_PTV0_70_CVetoBVeto', # Z->ee + jets with 0 < pT(Z) < 70 GeV whilst vetoing c and b-jets
                  'Zee_PTV70_140_CVetoBVeto', # Z->ee + jets with 70 < pT(Z) < 140 GeV whilst vetoing c and b-jets
                  'Zee_PTV140_280_CVetoBVeto', # Z->ee + jets with 140 < pT(Z) < 280 GeV whilst vetoing c and b-jets       
                  'Zee_PTV280_500_CVetoBVeto', # Z->ee + jets with 280 < pT(Z) < 500 GeV whilst vetoing c and b-jets
                  'Ztautau_PTV0_70_BFilter', # Z->ττ + jets with 0 < pT(Z) < 70 GeV and a requirement for b-jets
                  'Ztautau_PTV70_140_BFilter', # Z->ττ + jets with 70 < pT(Z) < 140 GeV and a requirement for b-jets
                  'Ztautau_PTV140_280_BFilter', # Z->ττ + jets with 140 < pT(Z) < 280 GeV and a requirement for b-jets
                  'Ztautau_PTV280_500_BFilter', # Z->ττ + jets with 280 < pT(Z) < 500 GeV and a requirement for b-jets
                  'Ztautau_PTV500_1000', # Z->ττ + jets with 500 < pT(Z) < 1000 GeV
                  'Ztautau_PTV1000_E_CMS'], # Z->ττ + jets with 1000 GeV < pT(Z) < centre-of-mass energy
    },

    'Other' : {
        'list' : ['ttW',
                  'lllv', # W(->lv)Z(->ll)
                  'ZqqZll', # Z(->qq)Z(->ll)
                  'llvv', # ZZ->llvv and WW->lvlv
                  'llll', # ZZ->llll
                  'single_top_wtchan', # Wt
                  'single_antitop_wtchan', # Wt
                  'ggH125_tautaull',
                  'VBFH125_tautaull',
                  'VBFH125_WW2lep',
                  'ggH125_WW2lep',
                  'WpH125J_qqWW2lep',
                  'ZH125J_qqWW2lep',
                  'ZH125J_vvWW2lep',
                  'WqqZll',
                  'WpqqWmlv',
                  'WplvWmqq',
                  'WlvZqq',
                  'lvvv',
                  'Wmunu_PTV0_70_CVetoBVeto',
                  'Wmunu_PTV0_70_CFilterBVeto',
                  'Wmunu_PTV0_70_BFilter',
                  'Wmunu_PTV70_140_CVetoBVeto',
                  'Wmunu_PTV70_140_CFilterBVeto',
                  'Wmunu_PTV70_140_BFilter',
                  'Wmunu_PTV140_280_CVetoBVeto',
                  'Wmunu_PTV140_280_CFilterBVeto',
                  'Wmunu_PTV140_280_BFilter',
                  'Wmunu_PTV280_500_CVetoBVeto',
                  'Wmunu_PTV280_500_CFilterBVeto',
                  'Wmunu_PTV280_500_BFilter',
                  'Wmunu_PTV500_1000',
                  'Wmunu_PTV1000_E_CMS',
                  'Wenu_PTV0_70_CVetoBVeto',
                  'Wenu_PTV0_70_CFilterBVeto',
                  'Wenu_PTV0_70_BFilter',
                  'Wenu_PTV70_140_CVetoBVeto',
                  'Wenu_PTV70_140_CFilterBVeto',
                  'Wenu_PTV70_140_BFilter',
                  'Wenu_PTV140_280_CVetoBVeto',
                  'Wenu_PTV140_280_CFilterBVeto',
                  'Wenu_PTV140_280_BFilter',
                  'Wenu_PTV280_500_CVetoBVeto',
                  'Wenu_PTV280_500_CFilterBVeto',
                  'Wenu_PTV280_500_BFilter',
                  'Wenu_PTV500_1000',
                  'Wenu_PTV1000_E_CMS',
                  'Wtaunu_PTV0_70_CVetoBVeto',
                  'Wtaunu_PTV0_70_CFilterBVeto',
                  'Wtaunu_PTV0_70_BFilter',
                  'Wtaunu_PTV70_140_CVetoBVeto',
                  'Wtaunu_PTV70_140_CFilterBVeto',
                  'Wtaunu_PTV70_140_BFilter',
                  'Wtaunu_PTV140_280_CVetoBVeto',
                  'Wtaunu_PTV140_280_CFilterBVeto',
                  'Wtaunu_PTV140_280_BFilter',
                  'Wtaunu_PTV280_500_CVetoBVeto',
                  'Wtaunu_PTV280_500_CFilterBVeto',
                  'Wtaunu_PTV280_500_BFilter',
                  'Wtaunu_PTV500_1000',
                  'Wtaunu_PTV1000_E_CMS',
                  'single_top_tchan',
                  'single_antitop_tchan',
                  'single_top_schan',
                  'single_antitop_schan'],
    },

}


def read_sample(s):
    print('Processing '+s+' samples')
    frames = []
    for val in samples[s]['list']:
        prefix = "MC/mc_"
        if s == 'data': prefix = "Data/"
        else: prefix += str(infofile.infos[val]["DSID"])+"."
        fileString = tuple_path+prefix+val+".exactly2lep.root" 
        if fileString != "":
            temp = read_file(fileString,val)
            frames.append(temp)
    data_s = pd.concat(frames)
    data_s['LepDeltaPhi'] = data_s['LepDeltaPhi'].round(2)
    data_s.to_csv('13TeV_ttZ.csv', mode='a', index=False, header=False)
    return data_s


def get_data_from_files():
    data = {}
    df=pd.DataFrame(columns=["type","Channel","NJets","MET","Mll","LepDeltaPhi","LepDeltaR","SumLepPt","NBJets","weight"])
    df.to_csv('13TeV_ttZ.csv',index=False)
    for s in samples:
        data[s] = read_sample(s)
    return data

# multiply event weights and scale factors
def calc_weight(mcWeight,scaleFactor_PILEUP,scaleFactor_ELE,
                scaleFactor_MUON, scaleFactor_LepTRIGGER):
    return mcWeight*scaleFactor_PILEUP*scaleFactor_ELE*scaleFactor_MUON*scaleFactor_LepTRIGGER


# multiply totalWeight by cross-section weight
def get_xsec_weight(totalWeight,sample):
    info = infofile.infos[sample]
    weight = (lumi*1000*info["xsec"])/(info["sumw"]*info["red_eff"]) #*1000 to go from fb-1 to pb-1
    weight *= totalWeight
    return round(weight/MC_to_data_ratio,5)
    #return weight/MC_to_data_ratio

def find_good_lep_i(i,lep_type,lep_pt,lep_eta,lep_ptcone,lep_etcone,lep_z0,lep_sigd0,lep_isTightID): # variables for good lepton
    if abs(lep_eta[i])<2.5 and lep_ptcone[i]<0.06*lep_pt[i] and lep_sigd0[i]<5 and lep_isTightID[i]: # |η|<2.5 & ptcone < 6% of pt & σ(d0)<5
        if lep_type[i]==11 and lep_etcone[i]>0.06*lep_pt[i]: # electron with etcone > 6% of pt
            return False # not good lepton
        if lep_type[i]==13 and lep_sigd0[i]>3: return False # not good lepton if muon with σ(d0)>3
        theta_i = 2*np.arctan(np.exp(-lep_eta[i])) # calculate theta angle
        if abs(lep_z0[i]*np.sin(theta_i))<0.5: # z0*sin(θ) < 0.5mm
            return True # good lepton if all these requirements are passed
    return False


# return number to represent which process
def mc_type(sample):
    if sample in samples['ttZ']['list']: return 1
    elif sample in samples['ttbar']['list']: return 2
    elif sample in samples['Z']['list']: return 3
    elif sample in samples['Other']['list']: return 4
    else: return 0 #data

# return number to represent which channel
def channel(lep_type):
    if lep_type[0]*lep_type[1]==121: return 0 #ee
    elif lep_type[0]*lep_type[1]==169: return 1 #mm
    else: return 2 #em 

# calculate invariant mass of dilepton pair
def calc_mll(lep_pt,lep_eta,lep_phi,lep_E):
    px_0 = lep_pt[0]*np.cos(lep_phi[0])
    py_0 = lep_pt[0]*np.sin(lep_phi[0])
    pz_0 = lep_pt[0]*np.sinh(lep_eta[0])
    px_1 = lep_pt[1]*np.cos(lep_phi[1])
    py_1 = lep_pt[1]*np.sin(lep_phi[1])
    pz_1 = lep_pt[1]*np.sinh(lep_eta[1])
    sumpx = px_0 + px_1
    sumpy = py_0 + py_1
    sumpz = pz_0 + pz_1
    sump = np.sqrt(sumpx**2 + sumpy**2 + sumpz**2)
    sumE = lep_E[0] + lep_E[1]
    return round(np.sqrt(sumE**2 - sump**2)/1000,2) #/1000 to go from MeV to GeV

# function to calculate ∆R separation between two objects
def calc_dRLL(lep_eta,lep_phi): # eta,phi of 2 objects
    delta_eta = lep_eta[0]-lep_eta[1] # Δη between the 2 objects
    delta_phi = lep_phi[0]-lep_phi[1] # Δϕ between the 2 objects
    if delta_phi >= np.pi: delta_phi -= 2*np.pi # use π periodicity to get number between -π and π
    elif delta_phi < -np.pi: delta_phi += 2*np.pi # use π periodicity to get number between -π and π
    return round(np.sqrt(delta_eta**2 + delta_phi**2),2) # return ∆R for this object

# calculate azimuthal angle difference between the 2 leptons
def calc_dPhiLL(lep_phi):
    dPhi = lep_phi[0]-lep_phi[1]
    if dPhi >= np.pi: dPhi -= 2*np.pi
    elif dPhi < -np.pi: dPhi += 2*np.pi
    return round(abs(dPhi),2)

# calculate the pt of the vector sum of the 2 leptons
def calc_ptLL(lep_pt,lep_phi):
    px_0 = lep_pt[0]*np.cos(lep_phi[0])
    py_0 = lep_pt[0]*np.sin(lep_phi[0])
    px_1 = lep_pt[1]*np.cos(lep_phi[1])
    py_1 = lep_pt[1]*np.sin(lep_phi[1])
    sumpx = px_0 + px_1
    sumpy = py_0 + py_1
    return round(np.sqrt(sumpx**2 + sumpy**2)/1000,2) #/1000 to go from MeV to GeV 
    
# cut on nth good lepton
def cut_good_lep(is_good_lep_i):
    # throw away if lep isn't good                                                
    return is_good_lep_i==False

# throw away events that don't have opposite-charge leptons
def cut_lep_charge(lep_charge):
    # throw away when sum of lepton charges is not equal to 0
    # first lepton is [0], 2nd lepton is [1]                                                                                                                          
    return lep_charge[0] + lep_charge[1] != 0

# cut on transverse momentum of the leptons
def cut_lep_pt(lep_pt):
    # throw away any events where lep_pt[0] < 30 GeV                                                                                                            
    # throw away any events where lep_pt[1] < 15 GeV                                                                                                                
    return lep_pt[0] < 30000 or lep_pt[1] < 15000


def calc_good_jet_n(jet_n,jet_pt,jet_eta,jet_jvt): # get index of nth good jet
    good_jet_n = 0 # start counter for number of good jets
    for i in range(jet_n): # loop over remaining jets after previous good jet
        if jet_pt[i]>25000: # minimum pt of 25 GeV
            if jet_pt[i]<60000 and abs(jet_eta[i])<2.4: # extra requirements for pt < 60 GeV and |η|<2.4
                if jet_jvt[i]<0.59: continue # if jvt<0.59, this isn't a good jet so continue to the next jet
            good_jet_n += 1 # increment number of good jets
    return good_jet_n # return number of good jets

# cut on number of good jets
def cut_good_jet_n(NJets):
    return NJets<3

def calc_bjet_n(jet_n,jet_pt,jet_eta,jet_jvt,jet_MV2c10): 
    bjet_n = 0 # start counter for number of good jets
    for i in range(jet_n): # loop over jets
        if jet_pt[i]>25000: # minimum pt of 25 GeV
            if jet_pt[i]<60000 and abs(jet_eta[i])<2.4: # extra requirements for pt < 60 GeV and |η|<2.4
                if jet_jvt[i]<0.59: continue # if jvt<0.59, this isn't a good jet so continue to the next jet
            if jet_MV2c10[i]>0.6459: # for 77% b-tag efficiency
                bjet_n += 1 # increment number of bjets
    return bjet_n # return number of bjets

# cut on number of b-jets
def cut_bjet_n(bjet_n):
    # throw away if fewer than 2 b-jets
    return bjet_n<1

# throw away events where Mll < 10 GeV
def Mll_cut_lower(Mll):
    return Mll<10

# throw away events where Mll > 105 GeV
def Mll_cut_upper(Mll):
    return Mll>105

# throw away events where SumLepPt > 200 GeV
def cut_SumLepPt(SumLepPt):
    return SumLepPt>200

# throw away events where MET > 200 GeV
def cut_met_et(met_et):
    return met_et>200*1000

# throw away events where weight is less than 0.00005
def cut_weight(weight):
    return abs(weight)<0.00005

def read_file(path,sample):
    start = time.time()
    print("\tProcessing: "+sample+" file")
    data_all = pd.DataFrame()
    mc = uproot.open(path)["mini"]
    numevents = uproot.numentries(path, "mini")
    if 'data' in sample: fraction_MC=fraction
    else: fraction_MC=fraction*MC_to_data_ratio
    entrystart=0
    entrystop=numevents*fraction_MC
    for data in mc.iterate(['lep_pt','lep_eta','lep_phi','lep_E','lep_charge','lep_type','lep_ptcone30',
                             'lep_etcone20','lep_z0','lep_tracksigd0pvunbiased','lep_isTightID',
                              'met_et','jet_n',
                              'jet_pt','jet_eta','jet_phi','jet_E','jet_jvt','jet_MV2c10',
                              'mcWeight','scaleFactor_PILEUP','scaleFactor_ELE','scaleFactor_MUON',
                              'scaleFactor_LepTRIGGER','scaleFactor_BTAG'], 
                           flatten=False, entrysteps=2212282, outputtype=pd.DataFrame, entrystart=entrystart, entrystop=entrystop):

        nIn = len(data.index)

        # decide whether lep[0] is a good lepton using the function find_good_lep_i defined above    
        data['is_good_lep_0'] = np.vectorize(find_good_lep_i)(0,data.lep_type,data.lep_pt,data.lep_eta,
                                                              data.lep_ptcone30,data.lep_etcone20,data.lep_z0,
                                                              data.lep_tracksigd0pvunbiased,data.lep_isTightID)
        
        # cut on whether 0th lepton is good
        fail = data[ np.vectorize(cut_good_lep)(data.is_good_lep_0) ].index # get events that fail this cut
        data.drop(fail, inplace=True) # drop events where lep[0] isn't good
        if len(data.index)==0: 
            print('\t\t', sample, 'finishes with no events')
            continue # move onto next batch if no events left
        #print('\t\t lep 0 is good \t\t\t\t',len(data.index))
        
        # decide whether lep[1] is a good lepton using the function find_good_lep_i defined above
        data['is_good_lep_1'] = np.vectorize(find_good_lep_i)(1,data.lep_type,data.lep_pt,data.lep_eta,
                                                              data.lep_ptcone30,data.lep_etcone20,data.lep_z0,
                                                              data.lep_tracksigd0pvunbiased,data.lep_isTightID)
        
        # cut on whether 1st lepton is good                                                                                                                                                    
        fail = data[ np.vectorize(cut_good_lep)(data.is_good_lep_1) ].index # get events that fail this cut
        data.drop(fail, inplace=True) # drop events where lep[1] isn't good
        if len(data.index)==0: 
            print('\t\t', sample, 'finishes with no events')
            continue # move onto next batch if no events left
        #print('\t\t lep 1 is good \t\t\t\t',len(data.index))

        # cut on lepton charge                                                                                                                
        fail = data[ np.vectorize(cut_lep_charge)(data.lep_charge) ].index # get events that fail this cut
        data.drop(fail, inplace=True) # drop events where leptons aren't of opposite charge
        if len(data.index)==0: 
            print('\t\t', sample, 'finishes with no events')
            continue # move onto next batch if no events left
        #print('\t\t leptons of opposite charge \t\t',len(data.index))

        #cut on the transverse momentum of the leptons
        fail = data[ np.vectorize(cut_lep_pt)(data.lep_pt) ].index # get events that fail this cut
        data.drop(fail,inplace=True) # drop events where leptons don't pass minimum pt requirements
        if len(data.index)==0: 
            print('\t\t', sample, 'finishes with no events')
            continue # move onto next batch if no events left
        #print('\t\t leptons pass minimum pt requirements \t',len(data.index))

        # cut on MET
        fail = data[ np.vectorize(cut_met_et)(data.met_et) ].index # get events that fail this cut
        data.drop(fail,inplace=True) # drop events where met > 200 GeV
        if len(data.index)==0:
            print('\t\t', sample, 'finishes with no events')
            continue # move onto next batch if no events left

        # label for each mc type
        data['type'] = np.vectorize(mc_type)(sample)

        # label for channel (ee, mm or em)
        data['Channel'] = np.vectorize(channel)(data.lep_type)

        # number of jets
        data['NJets'] = np.vectorize(calc_good_jet_n)(data.jet_n,data.jet_pt,data.jet_eta,data.jet_jvt)

        # cut on number of good jets
        fail = data[ np.vectorize(cut_good_jet_n)(data.NJets) ].index # get events that fail the cut
        data.drop(fail,inplace=True) # drop the events that have fewer than 6 jets 
        if len(data.index)==0: 
            print('\t\t', sample, 'finishes with no events')
            continue # move onto next batch if no events left
        #print('\t\t at least 6 jets \t\t\t',len(data.index))

        # MET
        data['MET'] = round(data['met_et']/1000,2)

        # calculation of 2-lepton invariant mass
        data['Mll'] = np.vectorize(calc_mll)(data.lep_pt,data.lep_eta,data.lep_phi,data.lep_E)
        fail = data[ np.vectorize(Mll_cut_lower)(data.Mll) ].index
        data.drop(fail, inplace=True)
        if len(data.index)==0: 
            print('\t\t', sample, 'finishes with no events')
            continue # move onto next batch if no events left
        fail = data[ np.vectorize(Mll_cut_upper)(data.Mll) ].index
        data.drop(fail, inplace=True)
        if len(data.index)==0: 
            print('\t\t', sample, 'finishes with no events')
            continue # move onto next batch if no events left

        # Angular separation between leptons
        data['LepDeltaPhi'] = np.vectorize(calc_dPhiLL)(data.lep_phi)

        # Angular separation between leptons and MET dPhi(MET,ll)
        data['LepDeltaR'] = np.vectorize(calc_dRLL)(data.lep_eta,data.lep_phi)

        # Sum of lepton pt
        data['SumLepPt'] = np.vectorize(calc_ptLL)(data.lep_pt,data.lep_phi)
        fail = data[ np.vectorize(cut_SumLepPt)(data.SumLepPt) ].index
        data.drop(fail, inplace=True)
        if len(data.index)==0: 
            print('\t\t', sample, 'finishes with no events')
            continue # move onto next batch if no events left

        # whether at least 1 jet is btagged
        data['NBJets'] = np.vectorize(calc_bjet_n)(data.jet_n,data.jet_pt,data.jet_eta,data.jet_jvt,data.jet_MV2c10)

        # cut on number of b-jets
        #fail = data[ np.vectorize(cut_bjet_n)(data.NBJets) ].index # get events that fail this cut
        #data.drop(fail,inplace=True) # drop the events with fewer than 2 b-jets
        #if len(data.index)==0: 
        #    print('\t\t', sample, 'finishes with no events')
        #    continue # move onto next batch if no events left
        #print('\t\t at least 2 b-jets \t\t\t',len(data.index))

        if 'data' not in sample:
            data['weight'] = np.vectorize(calc_weight)(data.mcWeight,data.scaleFactor_PILEUP,data.scaleFactor_ELE,data.scaleFactor_MUON,data.scaleFactor_LepTRIGGER)
            data['weight'] = np.vectorize(get_xsec_weight)(data.weight,sample)
            # throw away events with weight < 0.00005
            fail = data[ np.vectorize(cut_weight)(data.weight) ].index
            data.drop(fail, inplace=True)
            if len(data.index)==0:
                print('\t\t', sample, 'finishes with no events')
                continue # move onto next batch if no events left
        else:
            data['weight'] = 1

        data.drop(['is_good_lep_0','is_good_lep_1','lep_pt','lep_eta','lep_phi','lep_E','lep_charge','lep_type','lep_ptcone30',
                             'lep_etcone20','lep_z0','lep_tracksigd0pvunbiased','lep_isTightID',
                              'met_et','jet_n',
                              'jet_pt','jet_eta','jet_phi','jet_E','jet_jvt','jet_MV2c10',
                              'mcWeight','scaleFactor_PILEUP','scaleFactor_ELE','scaleFactor_MUON',
                              'scaleFactor_LepTRIGGER','scaleFactor_BTAG'], axis=1, inplace=True)

        nOut = len(data.index)
        data_all = data_all.append(data)
        elapsed = time.time() - start
        print("\t\t"+sample+" time taken: "+str(elapsed)+"s, nIn: "+str(nIn)+", nOut: "+str(nOut))
        print('\t\tsum of weights ',sum(data['weight'])) # print total weight for file
    return data_all


start = time.time()
data = get_data_from_files()
print('data events ',sum(data['data']['weight']))
MC_sum_weights = 0
for s in samples:
    if s!='data':
        MC_sum_weights += sum(data[s]['weight'])
print('MC sum of weights ',MC_sum_weights)
elapsed = time.time() - start
print("Time taken: "+str(elapsed))
