import subprocess
import GPU_manager
import time
import string
# using Popen may suit better here depending on how you want to deal
# with the output of the child_script.

epochs= {"lobster":40000,"grid":40000,"triangular_grid":4000,"ogbg-molbbbp":40000,"MUTAG":40000,"DD":40000,"IMDBBINARY":40000,"PTC":40000}
# epochs= {"lobster":1000,"grid":1000,"triangular_grid":1000,"ogbg-molbbbp":1000,"MUTAG":1000,"DD":1000,"IMDBBINARY":1000,"PTC":1000}
defaults = {"in_normed_layer":True,"EvalOnTest":"True", "graphEmDim":"128", "scheduler_type":"None", "lr":".001", "beta":"2", "LDP":True} # ,"beta":"1","lr" : str(0.002),"dataset" : "lobster"
kernl_types = [ "in_degree_dist","HistogramOfCycles"]
# gpus = [3,4,5,6,7]
# threshold = 32000
gpus = [1,0,2,3]
threshold = 18000
# binningStrategy = ["EqualWidth","EqualFreq","BounderBinner"]
label = "LDP_"
settings = {"-dataset":[ "grid", "MUTAG", "lobster","PTC", "IMDBBINARY"]}
epslion = [1,2,3,4,5,6]# LDP parameters
settings = {"-dataset":[ "grid", ]}
epslion = [3]# LDP parameters

attempt_num = 5
for e in epslion:
        for att in range(attempt_num):
            for arg in settings.keys():
                dir = arg[1:]+"/"
                common_swichs = ["python", "GlobalPrespective.py",  "-desc_fun"]+kernl_types

                for key in defaults:
                    common_swichs.append("-"+key)
                    common_swichs.append(str(defaults[key]))
                # adding lr and beta

                common_swichs.append("-epsilon")
                common_swichs.append(str(e))

                for choice in settings[arg]:
                    exclude = set(string.punctuation)
                    #path to write the result
                    ch = ''.join(ch for ch in str(choice) if ch not in exclude)
                    ch = ch.replace(" ","_")
                    dir_to_write_Graphs = dir  + "/" + ch+"___"+ label+"_""epsilon_"+str(e) +"_"+str(att)+"/"
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







