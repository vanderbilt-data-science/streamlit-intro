

#basic ds package imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay



def plot_multiple(indf, include=None, exclude=None, no_cols=3, figsize=(9,4)):
    
    #get subset
    plot_df = indf.select_dtypes(include=include) if include is not None else indf.select_dtypes(exclude=exclude)
    plot_type = 'cat' if 'object' in plot_df.dtypes.values else 'num'
    
    #setup subplots
    no_vars = len(plot_df.columns)
    pltsize = None if plot_type=='num' else figsize
    fig, ax = plt.subplots(1, no_vars, figsize=pltsize)
    plt_axs = zip(ax, plot_df.columns.tolist())
    
    #plot based on categorical vs numerical
    if plot_type=='num':
        for ax, col in plt_axs:
            plot_df[col].plot(kind='hist', ax=ax, figsize=figsize)
            ax.set_xlabel(col)
            plt.tight_layout()
    else:
        [plot_df.value_counts(col).plot(kind='bar', ax=ax, ylabel='Frequency') for ax, col in plt_axs]
        plt.tight_layout()
    
    return fig



def generate_test_data(pred_sz=30):
    
    #randomly generate probabilities
    probs = np.random.rand(pred_sz)
    
    #dummy assignment of actual with a bit of variance mixed in
    actual = probs>=0.72
    random_wrong = np.random.rand(pred_sz)<0.1
    actual[random_wrong] = ~actual[random_wrong]
    actual = actual.astype(int)
    
    #create preds df
    pred_df = pd.DataFrame({'.p0':1-probs, '.p1':probs, '.actual':actual})
    
    #return
    return(pred_df)



def tune_threshold(preds_df, threshold=0.5):
    
    #get threshold and convert to int
    preds_df['.pred_class'] = preds_df['.p1'] >= threshold
    preds_df['.pred_class'] = preds_df['.pred_class'].astype(int)
    
    #plot confusion matrix
    cm = confusion_matrix(preds_df['.actual'], preds_df['.pred_class'])
    disp = ConfusionMatrixDisplay(cm, display_labels=['male', 'female'])
    
    return disp



def penguins_predict(input_vec, thresh):
    
    pred_val = np.random.rand(1)
    return 'female' if pred_val >= thresh else 'male'

