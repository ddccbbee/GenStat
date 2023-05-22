import subprocess
import GPU_manager
import time
import string
# using Popen may suit better here depending on how you want to deal
# with the output of the child_script.

epochs= {"lobster":40000,"grid":40000,"triangular_grid":40000,"ogbg-molbbbp":40000,"MUTAG":40000,"DD":40000,"IMDBBINARY":40000,"PTC":40000}
defaults = {"in_normed_layer":True,"EvalOnTest":"True","steps_of_reachability":"3","arg_step_num":"2", "graphEmDim":"1024", "scheduler_type":"OneCyle", "LDP":False} # ,"beta":"1","lr" : str(0.002),"dataset" : "lobster"
kernl_types = [ "in_degree_dist","HistogramOfRandomWalks", "ReachabilityInKsteps","HistogramOfCycles"]
gpus = [3,4,5,6,7]
threshold = 32000
# binningStrategy = ["EqualWidth","EqualFreq","BounderBinner"]
label = "NewArchi_2Step_3Rech_"
# dataset = "DD" #"PVGAErandomGraphs"#"PVGAErandomGraphs"
# settings = {"-binningStrategy":["combineBinner","EqualWidth","EqualFreq"]}
# settings = {"-bin_num":["N", "sqrt_N"]}
# settings = {"-beta":["64"]}
# settings = {"-binningStrategy":[["EqualWidth","EqualFreq","BounderBinner"],["UniformBinner","EqualFreq","BounderBinner"],["EqualWidth","BounderBinner"],["EqualFreq","BounderBinner"],["BounderBinner","UniformBinner"]]}
# settings = {"-arg_step_num" :[ "4","6","8","16"]}
settings = {"-dataset":["lobster","grid","triangular_grid","ogbg-molbbbp","MUTAG","DD","IMDBBINARY","PTC"]}
# settings = {"-Model_seed":["984","12","123","24","42",5643]}
lr_s = {.0005,.002,.001}
beta_s = {1,20,100}
for lr in lr_s:
    for beta in beta_s:
        for arg in settings.keys():
            dir = arg[1:]+"/"
            common_swichs = ["python", "GlobalPrespective.py",  "-desc_fun"]+kernl_types

            for key in defaults:
                common_swichs.append("-"+key)
                common_swichs.append(str(defaults[key]))
            # adding lr and beta

            common_swichs.append("-beta")
            common_swichs.append(str(beta))
            common_swichs.append("-lr")
            common_swichs.append(str(lr))

            for choice in settings[arg]:
                exclude = set(string.punctuation)
                #path to write the result
                ch = ''.join(ch for ch in str(choice) if ch not in exclude)
                ch = ch.replace(" ","_")
                dir_to_write_Graphs = dir  + "/" + ch+"___"+ label+"_"+str(lr) +"_"+ str(beta)+ "/"
                print("the result will be written in: "+dir_to_write_Graphs)
                avail = GPU_manager.get_free_gpu(threshold=threshold, targets = gpus, check=60, every=1)
                print("Avaiable GPUs were: "+str(avail))
                args_ = []
                args_ += common_swichs+["-write_them_in", dir_to_write_Graphs] + ["-device"] + [
                    "cuda:" + str(avail[0])] + [arg]
                if type(choice) == list:
                    args_.extend(choice)
                else:
                    args_.append(choice)

                # set the epoch number for the dataset

                if "dataset" in defaults:
                    args_.append("-e")
                    args_.append(str(epochs[defaults["dataset"]]))
                elif arg =="-dataset":
                    args_.append("-e")
                    args_.append(str(epochs[choice]))

                # subprocess.call(args_)
                subprocess.Popen(args_)
                time.sleep(60)







