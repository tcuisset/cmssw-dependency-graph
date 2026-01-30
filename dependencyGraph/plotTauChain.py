from dependencyGraph.graph import *

G = load_graph("/grid_mnt/vol_home/llr/cms/cuisset/hgcal/tau/prod_taus_v3/producers_graph/dependency.dot")

to_remove = ['offlineBeamSpot',
 'offlinePrimaryVertices',
 'offlineSlimmedPrimaryVertices',
 'prunedGenParticles',
 'firstStepPrimaryVertices',
 'MeasurementTrackerEvent',
 'fixedGridRhoAll']
Gc = G.copy()
Gc.remove_nodes_from(to_remove)

def remove_sel(x):
    if x.endswith("SecondaryVertices") or "PrimaryVertices" in x: return True
    if x.startswith("slimmed") and not "tau" in x and not "Tau" in x: return True
    if x.startswith("ak") and x.endswith("PFJets"): return True
    return False
to_remove = set(["generalTracks",  "lostTracks", "muons", "packedPFCandidates", "slimmedPhotons", "slimmedElectrons","particleFlow", "gedPhotons", "gedGsfElectrons", "slimmedElectrons", ]).union(x for x in Gc.nodes() if remove_sel(x))
Gc.remove_edges_from(list((n, suc) for n in to_remove for suc in Gc.successors(n) ))
len(G), len(Gc), len(G.edges), len(Gc.edges)



plot(ancestors_up_to(Gc, "slimmedTaus", None), figsize=(40, 40))
# plot(ancestors_up_to(Gc, "slimmedTausBoosted", None), figsize=(40, 40))
plot(ancestors_up_to(Gc, "slimmedTausNoUTag", None), figsize=(30, 30))
plot(ancestors_up_to(Gc, "patTaus", None), figsize=(30, 20))