# coding=utf-8

import numpy as np
import pylab

def compare(computed, truth_value, name):
    if computed is None:
        print name, "pas encore implémenté (valeur reçu=None)"
        return

    try:
        assert computed.shape == truth_value.shape
        assert np.allclose(computed, truth_value)

        print name, "bonne"
    except:
        print "Mauvais calcul de", name
        print "calculé"
        print computed
        print "bonne valeur"
        print truth_value
        print "error ratio"
        print computed/truth_value

##
# La fonction teste prend en entrée:
#   etiquettesTest - les étiquettes de test
#   etiquettesPred - les étiquettes prédites
# et retourne une table présentant les résultats
###
def teste(etiquettesTest, etiquettesPred):

	n_classes = max(etiquettesPred)
	conf_matrix = np.zeros((n_classes,n_classes))

	for (test,pred) in zip(etiquettesTest, etiquettesPred):
		conf_matrix[test-1,pred-1] += 1

	return conf_matrix
	

def distribution(train, test, fct, n_points=50):

    train_test = np.vstack((train,test))
    (min_x1,max_x1) = (min(train_test[:,0]),max(train_test[:,0]))
    (min_x2,max_x2) = (min(train_test[:,1]),max(train_test[:,1]))

    xgrid = np.linspace(min_x1,max_x1,num=n_points)
    ygrid = np.linspace(min_x2,max_x2,num=n_points)

	# calcule le produit cartesien entre deux listes
    # et met les resultats dans un array
    thegrid = np.array(combine(xgrid,ygrid))

    les_sorties = fct(thegrid)

    # La grille
    # Pour que la grille soit plus jolie
    #props = dict( alpha=0.3, edgecolors='none' )
    pylab.scatter(thegrid[:,0],thegrid[:,1],c = les_sorties, s=50)
    # Les points d'entrainment
    pylab.scatter(train[:,0], train[:,1], marker = 'v', s=50)
    # Les points de test
    pylab.scatter(test[:,0], test[:,1], marker = 's', s=50)

    ## Un petit hack, parce que la fonctionalite manque a pylab...
    h1 = pylab.plot([min_x1], [min_x2], marker='o', c = 'w',ms=5) 
    h2 = pylab.plot([min_x1], [min_x2], marker='v', c = 'w',ms=5) 
    h3 = pylab.plot([min_x1], [min_x2], marker='s', c = 'w',ms=5) 
    handles = [h1,h2,h3]
    ## fin du hack

    pylab.axis('equal')
    pylab.show()

# fonction plot
def gridplot(classifieur,train,test,n_points=50):

    train_test = np.vstack((train,test))
    (min_x1,max_x1) = (min(train_test[:,0]),max(train_test[:,0]))
    (min_x2,max_x2) = (min(train_test[:,1]),max(train_test[:,1]))

    xgrid = np.linspace(min_x1,max_x1,num=n_points)
    ygrid = np.linspace(min_x2,max_x2,num=n_points)

	# calcule le produit cartesien entre deux listes
    # et met les resultats dans un array
    thegrid = np.array(combine(xgrid,ygrid))

    les_sorties = classifieur.compute_predictions(thegrid)
    classesPred = np.argmax(les_sorties, axis=1)+1 

    # La grille
    # Pour que la grille soit plus jolie
    #props = dict( alpha=0.3, edgecolors='none' )
    pylab.scatter(thegrid[:,0],thegrid[:,1],c = classesPred, s=50)
    # Les points d'entrainment
    pylab.scatter(train[:,0], train[:,1], c = train[:,-1], marker = 'v', s=50)
    # Les points de test
    pylab.scatter(test[:,0], test[:,1], c = test[:,-1], marker = 's', s=50)

    ## Un petit hack, parce que la fonctionalite manque a pylab...
    h1 = pylab.plot([min_x1], [min_x2], marker='o', c = 'w',ms=5) 
    h2 = pylab.plot([min_x1], [min_x2], marker='v', c = 'w',ms=5) 
    h3 = pylab.plot([min_x1], [min_x2], marker='s', c = 'w',ms=5) 
    handles = [h1,h2,h3]
    ## fin du hack

#    labels = ['grille','train','test']
#    pylab.legend(handles,labels)

    pylab.axis('equal')
    pylab.show()


## http://code.activestate.com/recipes/302478/
def combine(*seqin):
    '''returns a list of all combinations of argument sequences.
for example: combine((1,2),(3,4)) returns
[[1, 3], [1, 4], [2, 3], [2, 4]]'''
    def rloop(seqin,listout,comb):
        '''recursive looping function'''
        if seqin:                       # any more sequences to process?
            for item in seqin[0]:
                newcomb=comb+[item]     # add next item to current comb
                # call rloop w/ rem seqs, newcomb
                rloop(seqin[1:],listout,newcomb)
        else:                           # processing last sequence
            listout.append(comb)        # comb finished, add to list
    listout=[]                      # listout initialization
    rloop(seqin,listout,[])         # start recursive process
    return listout

