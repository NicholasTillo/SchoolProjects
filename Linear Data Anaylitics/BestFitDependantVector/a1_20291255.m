function [rmsvars lowndx rmstrain rmstest] = a2_20291255
% [RMSVARS LOWNDX RMSTRAIN RMSTEST]=A3 finds the RMS errors of
% linear regression of the data in the file "GOODS.CSV" by treating
% each column as a vector of dependent observations, using the other
% columns of the data as observations of independent varaibles. The
% individual RMS errors are returned in RMSVARS and the index of the
% smallest RMS error is returned in LOWNDX. For the variable that is
% best explained by the other variables, a 5-fold cross validation is
% computed. The RMS errors for the training of each fold are returned
% in RMSTEST and the RMS errors for the testing of each fold are
% returned in RMSTEST.
%
% INPUTS:
%         none
% OUTPUTS:
%         RMSVARS  - 1xN array of RMS errors of linear regression
%         LOWNDX   - integer scalar, index into RMSVALS
%         RMSTRAIN - 1x5 array of RMS errors for 5-fold training
%         RMSTEST  - 1x5 array of RMS errors for 5-fold testing

    filename = 'goods.csv';
    [rmsvars lowndx] = a2q1(filename);
    [rmstrain rmstest] = a2q2(filename, lowndx)

end

function [rmsvars lowndx] = a2q1(filename)
% [RMSVARS LOWNDX]=A2Q1(FILENAME) finds the RMS errors of
% linear regression of the data in the file FILENAME by treating
% each column as a vector of dependent observations, using the other
% columns of the data as observations of independent varaibles. The
% individual RMS errors are returned in RMSVARS and the index of the
% smallest RMS error is returned in LOWNDX. 
%
% INPUTS:
%         FILENAME - character string, name of file to be processed;
%                    assume that the first row describes the data variables
% OUTPUTS:
%         RMSVARS  - 1xN array of RMS errors of linear regression
%         LOWNDX   - integer scalar, index into RMSVALS

    % Read the test data from a CSV file; find the size of the data
    % %
    
    DataRaw = csvread(filename, 1, 1);
    Size = size(DataRaw,1);
    DataStandard = zscore(DataRaw);

    % Compute the RMS errors for linear regression
    colNum = size(DataRaw,2);
    %Check every column
    for idx = 1:colNum
        %Taking each column as the dependant variable, 
        C = DataStandard(:, idx);
        A = DataStandard;
        %Preform the linear regression
        A(:,idx) = [];
        w = A\C;
        Cpredicted = A*w;
        %Save the RMS to the vector rmsvars
        rmsvars(idx) = rms(Cpredicted - C);
    end

    %Get the minimum of all the RMS's and save the index
    [M,I] = min(rmsvars);
    lowndx = I;

    %Prepare data for the testing and visualization
    A = DataRaw;
    A(:,I) = [];
     C = DataRaw(:, I);
    w = A\C;
    CGuess = A*w;

    % Plot the results creating a 2 data set figure. 
    figure 
    plot(C)
    hold on
    plot(CGuess,'o')
    hold off
    title('Regression vs Dependant Column Vector (Copper)')
    xlabel("Time passed since 1990, Data Collected Quarterly")
    ylabel("Price of Copper")
    legend({'Dependant Values','Generated Values'},'Location','northwest')
    %Use this model in order to create the mean of the Copper comlumn, then
    %compare it to the calculated mean, 
    MVec = mean(DataRaw);
    Mval = MVec(I);
    Mmat = MVec;
    Mmat(I) = [];
    %Using the model created before,
    Predicted = Mmat*w;
    disp("rms Error of predicting the mean of Copper Price")
    disp(rms(Mval-Predicted))


end
function [rmstrain rmstest] = a2q2(filename,lowndx)
% [RMSTRAIN RMSTEST]=A3Q2(LOWNDX) finds the RMS errors of 5-fold
% cross-validation for the variable LOWNDX of the data in the file
% FILENAME. The RMS errors for the training of each fold are returned
% in RMSTEST and the RMS errors for the testing of each fold are
% returned in RMSTEST.
%
% INPUTS:
%         FILENAME - character string, name of file to be processed;
%                    assume that the first row describes the data variables
%         LOWNDX   - integer scalar, index into the data
% OUTPUTS:
%         RMSTRAIN - 1x5 array of RMS errors for 5-fold training
%         RMSTEST  - 1x5 array of RMS errors for 5-fold testing

    % Read the test data from a CSV file; find the size of the data
    % % 
    k = 5;
    DataRaw = csvread(filename, 1, 1);
    Size = size(DataRaw,1);
    %Randomize, 
    rng('Default');
    randidx = randperm(Size);
    DataRawRand = DataRaw(randidx(:),:);

    %Add in the intercept column.
    C = DataRawRand(:,lowndx);
    A = [DataRawRand(:,1:end) ones([Size, 1])];
    %Remove the dependant column from the matrix
    A(:, lowndx) = [];
    %Initialize the grouping variables, 
    GroupingSize = round(Size/k);
    StartIdx = 1;
    EndIdx = StartIdx + GroupingSize;

    for idx = 1:k
        %Split the matrix into 2 sections, A, which is all the independant
        %coulmsn, and C the dependant columns. 
        %Split those into 2 more sections, rows StartIdx through EndIDX are
        %in the testing groups. 
        ATrain = [A(1:StartIdx, :); A(EndIdx:end, :)];
        CTrain =[C(1:StartIdx, :); C(EndIdx:end, :)];
        %In order to not include column 1 in the trainging when doing the
        %first fold, we handle that edge case. 
        if StartIdx == 1
            ATrain = [A(EndIdx:end, :)];
            CTrain =[C(EndIdx:end, :)];
        end
        %If its the last fold, we make it go to the end instead of past the
        %end. 
        if EndIdx > Size
            EndIdx = Size;
        end 
        %Create Test Matrix
        ATest = [A(StartIdx:EndIdx,:)];
        CTest = [C(StartIdx:EndIdx,:)];
        %Create wieght vector
        w = ATrain\CTrain;
    
        %Calculate the RMS and append them to the corresponding returns
        rmstrain(idx) = rms(CTrain - ATrain*w);
        rmstest(idx) = rms(CTest - ATest*w);
        %Shift the section we are training 
        StartIdx = StartIdx + GroupingSize;
        EndIdx = EndIdx + GroupingSize;
    end
    %Display Data
    disp("The RMS values of the Trained Data Sets")
    disp(rmstrain)
     disp("The RMS values of the Tested Data Sets")
     disp(rmstest)
     disp("The Mean RMS Training Data")
     disp(mean(rmstrain))
     disp("The Mean RMS Testing Data")
     disp(mean(rmstest))
     disp("The SD RMS Training Data")
     disp(std(rmstrain))
     disp("The SD RMS Testing Data")
     disp(std(rmstest))




end

function [rmstrain,rmstest]=mykfold(Xmat, yvec, k_in)
% [RMSTRAIN,RMSTEST]=MYKFOLD(XMAT,yvec,K) performs a k-fold validation
% of the least-squares linear fit of yvec to XMAT. If K is omitted,
% the default is 5.
%
% INPUTS:
%         XMAT     - MxN data vector
%         yvec     - Mx1 data vector
%         K        - positive integer, number of folds to use
% OUTPUTS:
%         RMSTRAIN - 1xK vector of RMS error of the training fits
%         RMSTEST  - 1xK vector of RMS error of the testing fits

    % Problem size
    M = size(Xmat, 1);
    

    
    % Set the number of folds; must be 1<k<M
    if nargin >= 3 & ~isempty(k_in)
        k = max(min(round(k_in), M-1), 2);
    else
        k = 5;
    end

    % Initialize the return variables
    rmstrain = zeros(1, k);
    rmstest  = zeros(1, k);

    % Process each fold
    for ix=1:k
        % %
        % % STUDENT CODE GOES HERE: replace the next 5 lines with code to
        % % (1) set up the "train" and "test" indexing for "xmat" and "yvec"
        % % (2) use the indexing to set up the "train" and "test" data
        % % (3) compute "wvec" for the training data
        % %
        xmat_train  = [0 1];
        yvec_train  = 0;
        wvec = [0 0];
        xmat_test = [0 1];
        yvec_test = 0;

        rmstrain(ix) = rms(xmat_train*wvec - yvec_train);
        rmstest(ix)  = rms(xmat_test*wvec  - yvec_test);
    end

end
