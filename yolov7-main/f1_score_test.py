y_true = [1,1,1,0,0]
y_pred = [1,0,1,0,1]

def precision(true, pred, positive_label=1):
    true_positive = 0 #초기화
    false_positive = 0
    for (i, p) in enumerate(pred):
        if p == positive_label and true[i] == positive_label: #TP
            true_positive += 1
        elif p == positive_label and true[i] != positive_label: #FP
            false_positive += 1
        
    return true_positive/(true_positive+false_positive)

def recall(true, pred, positive_label=1):
    true_positive = 0 #초기화
    false_positive = 0
    for (i, p) in enumerate(pred):
        if p == positive_label and true[i] == positive_label: #TP
            true_positive += 1
        elif p != positive_label and true[i] == positive_label: #FN
            false_positive += 1

    return true_positive/(true_positive+false_positive)

def f1_score(true, pred, positive_label=1):
    p = precision(true, pred, positive_label)
    r = recall(true, pred, positive_label)
    # return 2./(1/p + 1/r)
    return 2.*((p*r)/(p+r))

print('precision',precision(y_true, y_pred))
print('recall',recall(y_true, y_pred))
print('f1 score',f1_score(y_true, y_pred))

# import sklearn.metrics as met
# print(met.f1_score(y_true,y_pred))
