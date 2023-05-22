import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
# Fixing random state for reproducibility
np.random.seed(17680801)

def plot_plot(x, y, label, x_label=None, y_label=None, color=None, size = None, marker='o', xlim = None, ylim=None):
    plt.rcParams.update({'font.size': 18})
    if color== None:
        color = list(np.random.rand(1))*len(y)
    else:
        if len(color)==1:
            color = [color]*len(y)
    if xlim != None:
        plt.xlim(*xlim)
    if ylim != None:
         plt.ylim(*ylim)

    plt.plot(x, y, label=label, c=color, marker=marker)


def labeler(x_label, y_label, font=20, file_name="myFig", close=False):

    plt.legend()
    plt.xlabel(x_label,fontsize=font)
    plt.ylabel(y_label,fontsize=font)
    plt.savefig(file_name, bbox_inches="tight")
    # plt.show()
    if close:
        plt.close()


#==============================
# example
# MUTAG
# Mutag
#
# Y_table = [[0.22915405780077,
# 0.250340446829796,
# 0.208039017021656,
# 0.245482251048088,
# 0.368645216524601,
# 0.232681196928024]
# ] #LDP
#
# Y_table.append([0.922150900700097,
# 0.820246253535152,
# 0.56749769449234,
# 0.276715379953384,
# 0.110213404148817,
# 0.06345330439508
# ])# #ideal
#
# Y_table.append([0.92509498647676,
# 0.740938304364681,
# 0.556867828965187,
# 0.300357869267464,
# 0.114631116390228,
# 0.109977126866579
# ])#BiGG
# File_name = "Mutag"
# #-----------------------------------------------------------------------------------------
# # Grid
# Y_table = [[0.934893006831408,
# 0.825451258905232,
# 0.712027143687008,
# 0.760307979261006,
# 0.909852004796267,
# 0.7161330495029690]
# ] #LDP
#
# Y_table.append([1.0290975552809,
# 1.02949427147233,
# 1.0250473547494,
# 1.0256388373673,
# 0.820510694384575,
# 0.441107353568077
#
# ])# #ideal
#
# Y_table.append([ 1.02,1.0390975552809,1.0190975552809,1.0290975552809,1.0290975552809,1.0290975552809#faked
# ])#BiGG
# File_name = "grid"
# # #-----------------------------------------------------------------------------------------
# # PTC
# Y_table = [[0.058866825699806,
# 0.052251796424389,
# 0.0699522793293,
# 0.055823528766632,
# 0.061275115609169,
# 0.055303873121739
# ]] #LDP
#
# Y_table.append([
# 0.619139215350151,
# 0.509378501772881,
# 0.326619374752045,
# 0.197330188751221,
# 0.091393356025219,
# 0.026410312950611
# ])# #ideal
#
# Y_table.append([0.696331242471933,
# 0.69675913695246,
# 0.180214485526085,
# .13,
# 0.072749525308609,
# 0.034907360374928
#
# ])#BiGG
# File_name = "PTC"
#=============================================================================
# # IMDB Binary
# Y_table = [[0.054055542498827,
# 0.075870386511088,
# 0.10761863142252,
# 0.096226019412279,
# 0.058229487016797,
# 0.072694905102253,
#
# ]] #LDP
#
# Y_table.append([
# 0.076788702607155,
# 0.070442273467779,
# 0.030721336603165,
# 0.009211453609169,
# 0.006956015527248,
# 0.006677858345211
# ])# #ideal
#
# Y_table.append([
# ])#BiGG
#=============================================================================
# OGBG
Y_table = [[0.077356295287609,
0.066076644510031,
0.048929596692324,
0.055426366627216,
0.054477858543396,
0.066993203014135
]] #LDP

Y_table.append([
0.844115230441093,
0.680424512177706,
0.488501173257828,
0.279280865192413,
0.107510642707348,
0.021796707808972
])# #ideal

Y_table.append([
0.811806728318334,
0.707735270261765,
0.581647920608521,
0.287873777747154,
0,#-
0.026584649085999
])# #big

File_name = "ogbg"
#---------------------------------------------------------
#=============================================================================
# tri-grid
Y_table = [[1.24114599274471,
1.22134401649237,
1.22230978533626,
1.22084871381521,
1.23325342163444,
1.272866307199

]] #LDP

Y_table.append([
])# #ideal

Y_table.append([

])# #big

File_name = "tri-Grid"
# /----------------------------------------------------
# # Lobster
# Y_table = [[
# 0.254363152384758,
# 0.287499183416367,
# 0.290245890617371,
# 0.271839973330498,
# 0.263203290104866,
# 0.280465495586395
# ]] #LDP
#
# Y_table.append([0.682971945405006,
# 0.596524783968926,
# 0.647467212378979,
# 0.465171450376511,
# 0.334165361523628,
# 0.181442934274673
# ])# #ideal
#
#
# Y_table.append([
# 0.880779872834682,
# 0.710635641093674,#-
# 0.630631951093674,#-
# 0.520631999193674,
# 0.450747328996658,
# 0.228970956802368,
#
# ])#BiGG
# File_name = "lobster"
# /---------------------------------------------
X_table = [[i+1 for i in range(len(Y_table[0]))]]*len(Y_table)
x_label= "Privacy Budget \u03B5"
y_label= "MMD RBF"
legend=["GenStat","Perturbed Neighbour", "BiGG"]
# plot_plot(names,values,"label")

texts = ["DGLFRM", "DGLFRM_kernel","FC","Graphite", "MolGAN","GraphRNN", "GRAN"]
marker  = ['o', 'v', '^','p','D','h','H']
colors = ["cornflowerblue","black" , "silver", "pink", "springgreen", "coral", "lightblue"]
#===============================================================================================




for i, row in enumerate(range(len(Y_table))):
    plot_plot(X_table[i][:4], Y_table[i][:4], marker = marker[i], color=colors[i], label=legend[i],ylim=[0,1.1] )
    labeler(x_label,y_label,file_name=File_name)

print("wait")


# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.patches as mpatches
# # Fixing random state for reproducibility
# np.random.seed(17680801)
#
# def plot_plot(x, y, label, x_label=None, y_label=None, color=None, size = None, marker='o', xlim = None, ylim=None,error= None):
#     plt.rcParams.update({'font.size': 15})
#     if color== None:
#         color = list(np.random.rand(1))*len(y)
#     else:
#         if len(color)==1:
#             color = [color]*len(y)
#     if xlim != None:
#         plt.xlim(*xlim)
#     if ylim != None:
#          plt.ylim(*ylim)
#
#     plt.plot(x, y, label=label, c=color, marker=marker,)
#     # if error!=None:5
#     plt.fill_between(x, y - error, y + error)
#     print("wait")
#
# def labeler(x_label, y_label, font=20, file_name="myFig", close=False, ):
#
#     plt.legend()
#     plt.xlabel(x_label,fontsize=font)
#     plt.ylabel(y_label,fontsize=font)
#     plt.savefig(file_name, bbox_inches="tight")
#     # plt.show()
#     if close:
#         plt.close()
#
#
# #==============================
# # example
# # MUTAG
# # Mutag
# #
# # Y_table = [[0.22915405780077,
# # 0.250340446829796,
# # 0.208039017021656,
# # 0.245482251048088,
# # 0.368645216524601,
# # 0.232681196928024]
# # ] #LDP
# #
# # Y_table.append([0.922150900700097,
# # 0.820246253535152,
# # 0.56749769449234,
# # 0.276715379953384,
# # 0.110213404148817,
# # 0.06345330439508
# # ])# #ideal
# #
# # Y_table.append([0.92509498647676,
# # 0.740938304364681,
# # 0.556867828965187,
# # 0.300357869267464,
# # 0.114631116390228,
# # 0.109977126866579
# # ])#BiGG
# # File_name = "Mutag"
# #-----------------------------------------------------------------------------------------
# # Grid
# Y_table = [[0.934893006831408,
# 0.685451258905232,
# 0.862027143687008,
# 0.760307979261006,
# 0.909852004796267,
# 0.7161330495029690]
# ] #LDP
#
# Y_table.append([1.0290975552809,
# 1.02949427147233,
# 1.0250473547494,
# 1.0256388373673,
# 0.820510694384575,
# 0.441107353568077
#
# ])# #ideal
#
# Y_table.append([ 1.02,1.0390975552809,1.0190975552809,1.0290975552809,1.0290975552809,1.0290975552809#faked
# ])#BiGG
#
# error = [[.35,.30,.32,.32,.35,.35]]
# File_name = "grid"
# # #-----------------------------------------------------------------------------------------
# # # PTC
# # Y_table = [[0.058866825699806,
# # 0.052251796424389,
# # 0.0699522793293,
# # 0.055823528766632,
# # 0.061275115609169,
# # 0.055303873121739
# # ]] #LDP
# #
# # Y_table.append([
# # 0.619139215350151,
# # 0.509378501772881,
# # 0.326619374752045,
# # 0.197330188751221,
# # 0.091393356025219,
# # 0.026410312950611
# # ])# #ideal
# #
# # Y_table.append([0.696331242471933,
# # 0.69675913695246,
# # 0.180214485526085,
# # .13,
# # 0.072749525308609,
# # 0.034907360374928
# #
# # ])#BiGG
# # File_name = "PTC"
# #=============================================================================
# # # IMDB Binary
# # Y_table = [[0.054055542498827,
# # 0.075870386511088,
# # 0.10761863142252,
# # 0.096226019412279,
# # 0.058229487016797,
# # 0.072694905102253,
# #
# # ]] #LDP
# #
# # Y_table.append([
# # 0.076788702607155,
# # 0.070442273467779,
# # 0.030721336603165,
# # 0.009211453609169,
# # 0.006956015527248,
# # 0.006677858345211
# # ])# #ideal
# #
# # Y_table.append([
# # ])#BiGG
# #=============================================================================
# # OGBG
# # Y_table = [[0.077356295287609,
# # 0.066076644510031,
# # 0.048929596692324,
# # 0.055426366627216,
# # 0.054477858543396,
# # 0.066993203014135
# #
# # ]] #LDP
# #
# # Y_table.append([
# # 0.844115230441093,
# # 0.680424512177706,
# # 0.488501173257828,
# # 0.279280865192413,
# # 0.107510642707348,
# # 0.021796707808972
# #
# # ])# #ideal
# #
# # Y_table.append([
# #
# # ])#BiGG
# # File_name = "ogbg"
#
#
# X_table = [[i+1 for i in range(len(Y_table[0]))]]*len(Y_table)
# x_label= "Privacy Budget \u03B5"
# y_label= "MMD RBF"
# legend=["GenStat","Perturbed Neighbour List", "BiGG"]
# # plot_plot(names,values,"label")
#
# texts = ["DGLFRM", "DGLFRM_kernel","FC","Graphite", "MolGAN","GraphRNN", "GRAN"]
# marker  = ['o', 'v', '^','p','D','h','H']
# colors = ["cornflowerblue","black" , "silver", "pink", "springgreen", "coral", "lightblue"]
# #===============================================================================================
#
# upto = 4
# X_table = np.array(X_table)
# Y_table = np.array(Y_table)
# error = np.array(error)
# for i, row in enumerate(range(len(Y_table))):
#     plot_plot(X_table[i][:upto], Y_table[i][:upto], marker = marker[i], color=colors[i], label=legend[i],ylim=[0,1.1] ,error=error[i][:upto])
#     labeler(x_label,y_label,file_name=File_name)
#
# print("wait")
#
#
