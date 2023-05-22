# GenStat
## code overview
The file "GlobalPrespective.py" includes the training pipeline as well as the implementation of  the objective function. Source codes for loading the real and synthetic graphs are included in "data.py". 
"data/LDP/" contains the perturbed adjacency matrices used for graph generation with LDP guarantee. All the Python packages used in our experiments are provided in "requirement.yml".
Generated graph samples for GenStat are provided in the "ReportedResult/" directory, both in the pickle and png format. \url{https://drive.google.com/drive/folders/1mF-kU021-ceNh6ejLgf41sSE9FEzc01Q} contains the generated samples by the baselines. 
We used "GraphGenerationWithLDP.py" and "GraphGeneration.py" for the GenStat's reported result in the Sec. 4. These files contain the necessary commands and hyperparameters used in the experiments.
