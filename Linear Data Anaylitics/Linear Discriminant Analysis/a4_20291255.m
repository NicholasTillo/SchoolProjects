function a4_20291255

%TO DO, ROC CURVE AND CONFORM, 


% Function for CISC271, Winter 2022, Assignment #4

    % Read the test data from a CSV file
    dmrisk = csvread('dmrisk.csv',1,0);

    % Columns for the data and labels; DM is diabetes, OB is obesity
    jDM = 17;
    jOB = 16;

    % Extract the data matrices and labels
    XDM = dmrisk(:, (1:size(dmrisk,2))~=jDM);
    yDM = dmrisk(:,jDM);
    XOB = dmrisk(:, (1:size(dmrisk,2))~=jOB);
    yOB = dmrisk(:,jOB);

    % Reduce the dimensionality to 2D using PCA
    [~,rDM] = pca(zscore(XDM), 'NumComponents', 2);
    [~,rOB] = pca(zscore(XOB), 'NumComponents', 2);

    % Find the LDA vectors and scores for each data set
    [qDM zDM qOB zOB] = a4q1(rDM, yDM, rOB, yOB);
    disp("LDA scores for diabeties dataset")
    disp("qDM = ")
    disp(qDM)
    disp("zDM = ")
    disp(zDM)
    disp("LDA scores for obesity Dataset")
    disp("qOB = ")
    disp(qOB)
    disp("zOB = ")
    disp(zOB)


    % %
    % % STUDENT CODE GOES HERE: PLOT RELEVANT DATA
    % %
    q1 = ones(size(zDM, 1),1);
    q1(yDM == 1) = -1;
    q2 = ones(size(zOB, 1),1);
    q2(yOB == 1) = -1;
    %plot the LDA dimesion reduction
    figure
    gscatter(zDM,q1, yDM)
    figure
    gscatter(zOB, q2, yOB)

    % Compute the ROC curve and its AUC where: "xroc" is the horizontal
    % axis of false positive rates; "yroc" is the vertical
    % axis of true positive rates; "auc" is the area under curve
    % %
    % % STUDENT CODE GOES HERE: COMPUTE, PLOT, DISPLAY RELEVANT DATA
    % %
    %Plot diabeties ROC cure
    [xroc,yroc,auc,bopt] = roccurve(yDM, zDM);
    disp("bopt of diabeties dataset = ")
    disp(bopt)
    disp("AUC = ")
    disp(auc)
    figure
    hold on
    scatter(xroc,yroc)
    xlabel('FPR of LDA on Diabeties Data') 
    ylabel('TPR of LDA on Diabeties Data')
    x = 0:1;
    y = 0:1;
    plot(x, y)
    hold off

    %Plot Obesity ROC curve
    [xroc,yroc,auc,bopt] = roccurve(yOB, zOB);
    disp("bopt of obesity dataset = ")
    disp("AUC = ")
    disp(auc)
    disp(bopt)
    figure
    hold on
    scatter(xroc,yroc)
    xlabel('FPR of LDA on Obesity Data') 
    ylabel('TPR of LDA on Obesity Data')
    x = 0:1;
    y = 0:1;
    plot(x, y)
    hold off




    


% END OF FUNCTION
end

function [q1, z1, q2, z2] = a4q1(Xmat1, yvec1, Xmat2, yvec2)
% [Q1 Z1 Q2 Z2]=A4Q1(X1,Y1,X2,Y2) computes an LDA axis and a
% score vector for X1 with Y1, and for X2 with Y2.
%
% INPUTS:
%         X1 - MxN data, M observations of N variables
%         Y1 - Mx1 labels, +/- computed as ==/~= 1
%         X2 - MxN data, M observations of N variables
%         Y2 - Mx1 labels, +/- computed as ==/~= 1
% OUTPUTS:
%         Q1 - Nx1 vector, LDA axis of data set #1
%         Z1 - Mx1 vector, scores of data set #1
%         Q2 - Nx1 vector, LDA axis of data set #2
%         Z2 - Mx1 vector, scores of data set #2

    q1 = [];
    z1 = [];
    q2 = [];
    z2 = [];
    
    % Compute the LDA axis for each data set
    q1 = lda2class(Xmat1(yvec1==1,:), Xmat1(yvec1~=1, :));
    q2 = lda2class(Xmat2(yvec2==1,:), Xmat2(yvec2~=1, :));
   
    % %
    % % STUDENT CODE GOES HERE: COMPUTE SCORES USING LDA AXES
    % %
    z1 = (Xmat1 - ones(size(Xmat1, 1), 1)*mean(Xmat1))*q1;
    z2 = (Xmat2 - ones(size(Xmat2, 1), 1)*mean(Xmat2))*q2;
    
% END OF FUNCTION
end

function qvec = lda2class(X1, X2)
% QVEC=LDA2(X1,X2) finds Fisher's linear discriminant axis QVEC
% for data in X1 and X2.  The data are assumed to be sufficiently
% independent that the within-label scatter matrix is full rank.
%
% INPUTS:
%         X1   - M1xN data with M1 observations of N variables
%         X2   - M2xN data with M2 observations of N variables
% OUTPUTS:
%         qvec - Nx1 unit direction of maximum separation

    qvec = ones(size(X1,2), 1);
    xbar1 = mean(X1);
    xbar2 = mean(X2);
    xbar = mean([X1; X2]);

    % Compute the within-class means and scatter matrices
    % %
    % % STUDENT CODE GOES HERE: COMPUTE S1, S2, Sw
    % %
    M1 = X1 - ones(size(X1, 1), 1)*xbar1;
    M2 = X2 - ones(size(X2, 1), 1)*xbar2;

    S1 = M1'*M1;
    S2 = M2'*M2;
    Sw = S1 + S2;
    % Compute the between-class scatter matrix
    % %
    % % STUDENT CODE GOES HERE: COMPUTE Sb
    % %
    T = [xbar1 - xbar; xbar2 - xbar];
    Sb = T'*T;

    % Fisher's linear discriminant is the largest eigenvector
    % of the Rayleigh quotient
    % %
    % % STUDENT CODE GOES HERE: COMPUTE qvec
    % %
    [eigvecs, ~] = eig(inv(Sw)*Sb);
    qvec = eigvecs(:,1);

    % May need to correct the sign of qvec to point towards mean of X1
    if (xbar1 - xbar2)*qvec < 0
        qvec = -qvec;
    end
% END OF FUNCTION
end

function [fpr tpr auc bopt] = roccurve(yvec_in,zvec_in)
% [FPR TPR AUC BOPT]=ROCCURVE(YVEC,ZVEC) computes the
% ROC curve and related values for labels YVEC and scores ZVEC.
% Unique scores are used as thresholds for binary classification.
%
% INPUTS:
%         YVEC - Mx1 labels, +/- computed as ==/~= 1
%         ZVEC - Mx1 scores, real numbers
% OUTPUTS:
%         FPR  - Kx1 vector of False Positive Rate values
%         TPR  - Kx1 vector of  True Positive Rate values
%         AUC  - scalar, Area Under Curve of ROC determined by TPR and FPR
%         BOPT - scalar, optimal threshold for accuracy

    % Sort the scores and permute the labels accordingly
    [zvec zndx] = sort(zvec_in);
    yvec = yvec_in(zndx);
        
    % Sort and find a unique subset of the scores; problem size
    bvec = unique(zvec);
    bm = numel(bvec);
    
    % Compute a confusion matrix for each unique threshold value;
    % extract normalized entries into TPR and FPR vectors; track
    % the accuracy and optimal B threshold

    %initialize Values
    tpr = [];
    fpr = [];
    acc = -inf;
    bopt = -inf;
    fargle = [];
    for jx = 1:bm
        % %
        % % STUDENT CODE GOES HERE: FIND TPR, FPR, OPTIMAL THRESHOLD
        % %
        cmat = [];
        tempAcc = 0;
        cmat = confmat(yvec, bvec, bvec(jx));
        %Gather Values to use later, 
        Tp = cmat(1,1);
        Fp = cmat(2,1);
        Tn = cmat(2,2);
        Fn = cmat(1,2);
        %Gather more values
        tprTemp = (Tp) / (Tp + Fn);
        fprTemp = (Fp) / (Tn + Fp); 
        fnrTemp = (Tn) / (Tn + Fn);
        tnrTemp = (Fn) / (Tn + Fn);
        %Append the TPR and FPR to the list, to plot later
        tpr = [tpr; tprTemp];
        fpr = [fpr; fprTemp];

        %Gather the optimal threshold. 
        BestThreshold = ((tprTemp * tnrTemp) - (fnrTemp * fprTemp));
        tempAcc = (Tp + Tn) ./ (Tp + Fn + Tn + Fp);
        %If the current accruacy is higher than the highest accuracy, swap
        %them and save the threshold used. 
        if acc < tempAcc
            acc = tempAcc;
            bopt = bvec(jx);
            fargle = cmat;
        end
    end
    %Display the highest accuracy confusion matirx. 
    disp(fargle)

    % Ensure that the rates, from these scores, will plot correctly
    tpr = sort(tpr);
    fpr = sort(fpr);
    
    % Compute and display AUC for this ROC

    auc = aucofroc(fpr, tpr);
    
end
    
function cmat = confmat(yvec, zvec, theta)
% CMAT=CONFMAT(YVEC,ZVEC,THETA) finds the confusion matrix CMAT for labels
% YVEC from scores ZVEC and a threshold THETA. YVEC is assumed to be +1/-1
% and each entry of ZVEC is scored as -1 if <THETA and +1 otherwise. CMAT
% is returned as [TP FN ; FP TN]
%
% INPUTS:
%         YVEC  - Mx1 values, +/- computed as ==/~= 1
%         ZVEC  - Mx1 scores, real numbers
%         THETA - threshold real-valued scalar
% OUTPUTS:
%         CMAT  - 2x2 confusion matrix; rows are +/- labels,
%                 columns are +/- classifications

    % Find the plus/minus 1 vector of quantizations
    qvec = sign((zvec >= theta) - 0.5);
    cmat = zeros(2,2);

    % Compute the confusion matrix by entries
    % %
    % % STUDENT CODE GOES HERE: COMPUTE MATRIX
    % %
    %For each of the data pairings, incriment the corresponding value in
    %the confusion matrix
    for idx = 1:size(qvec,1)
        if qvec(idx) == yvec(idx) && qvec(idx) == 1
            cmat(1,1) = cmat(1,1) + 1;
        elseif qvec(idx) < yvec(idx)
            cmat(1,2) = cmat(1,2) + 1;
        elseif qvec(idx) > yvec(idx)
            cmat(2,1) = cmat(2,1) + 1;
        else
            cmat(2,2) = cmat(2,2) + 1;
        end

    end 

end

function auc = aucofroc(fpr, tpr)
% AUC=AUCOFROC(TPR,FPR) finds the Area Under Curve of the
% ROC curve specified by the TPR, True Positive Rate, and
% the FPR, False Positive Rate.
%
% INPUTS:
%         TPR - Kx1 vector, rate for underlying score threshold 
%         FPR - Kx1 vector, rate for underlying score threshold 
% OUTPUTS:
%         AUC - integral, from Trapezoidal Rule on [0,0] to [1,1]

    [X undx] = sort(reshape(fpr, 1, numel(fpr)));
    Y = sort(reshape(tpr(undx), 1, numel(undx)));
    auc = abs(trapz([0 X 1] , [0 Y 1]));
end
