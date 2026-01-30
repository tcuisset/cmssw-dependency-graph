# cmssw-dependency-graph
Making graph visualizations of CMSSW chain of EDProducer (tracking consumes relationships)

## How-to use
### Step 1 : make dot file
Add to a cmsRun config file `process.load("FWCore.Services.DependencyGraph_cfi")` ([TWiki](https://twiki.cern.ch/twiki/bin/view/CMSPublic/DependencyGraph)). 
Then run `cmsRun` the usual way (just one event is enough) and a `dependency.dot` will be produced, containing a graph with each EDProducer as node and edges representing "consumes" relationships.

#### extra settings
Adding `process.DependencyGraph.showPathDependencies = False` will avoid putting "Path" dependencies (ie not actual event products) in the graph.
ALso look at printDependencies of process.options


### Step 2 : viewing the graph
The `dependency.dot` file is in standard 'dot' format (from graphviz program). Standard tools can be used to visualize it.
Example : `sfdp -x -Goverlap=scale -Tpng dependency.dot -o dependency.png`
(for full RECO will be extremly large).
For viewing large graphs one can use gephi or other graph vis program.
There are also python tools in this repository to prune the graph to focus only on interesting parts.

## Tips
If one is only interested in one part of the reconstruction chain, it is useful to remove all non-needed chains from the schedule & output.
For example, if one is only interested in taus : 
~~~py
process.MINIAODSIMoutput.outputCommands = [
    "drop *",
    'keep *_slimmedTaus_*_*',
    'keep *_slimmedTausBoosted_*_*',
]
~~~
Also removing DQM output is useful (in case one is not interested by VALIDATION chain).