function a3_20291255
% Function for CISC271, Winter 2022, Assignment #3

    % %
    % % STUDENT CODE GOES HERE: REMOVE THIS COMMENT
    % % Read the test data from a CSV file
    read = csvread("wine.csv", 0,1);
    
    cultivar = read(1,:);
    data = read(2:end,:);
    data = transpose(data);
    cultivar = transpose(cultivar);

    % % Extract the data matrix and the Y cluster identifiers
    ZeroMData = data - mean(data);
    zData = zscore(data);



     % % Compute the pair of columns of Xmat with the lowest DB index
    min = 0;
    minColumns = [];
    for idx = 1:size(data,2)
        for l = idx+1:size(data,2)
            z = false(size(data,2),1);
            z(idx) = true;
            z(l) = true;
            minData = data(:,z);
            val = dbindex(minData, cultivar);
            if min == 0
                min = val;
                minColumns = z;
            end
            if val < min
                min = val;
                minColumns = z;
            end
        end
    end
    
    avec = data(:,minColumns);
    column4 = avec(:,1);
    column11 = avec(:,2);

    gscatter(column4,column11,cultivar)
   
    
    
    % % Compute the PCA's of the data using the SVD; score the clusterings
    [U,S,V] = svd(ZeroMData);
    Z1 = ZeroMData*V(:,1);
    Z2 = ZeroMData*V(:,2);
    xmmx = [Z1,Z2];
    dbData = dbindex(xmmx, cultivar);
    gscatter(Z1,Z2,cultivar)
%
    % % Standarize the data, then find score based on that.
    [sU,sS,sV] = svd(zData);
    sZ1 = zData*sV(:,1);
    sZ2 = zData*sV(:,2);
    sxmmx = [sZ1,sZ2];
    dbStandard = dbindex(sxmmx, cultivar);
    gscatter(sZ1,sZ2,cultivar)
     
   

end
function score = dbindex(Xmat, lvec)
% SCORE=DBINDEX(XMAT,LVEC) computes the Davies-Bouldin index
% for a design matrix XMAT by using the values in LVEC as labels.
% The calculation implements a formula in their journal article.
%
% INPUTS:
%        XMAT  - MxN design matrix, each row is an observation and
%                each column is a variable
%        LVEC  - Mx1 label vector, each entry is an observation label
% OUTPUT:
%        SCORE - non-negative scalar, smaller is "better" separation

    % Anonymous function for Euclidean norm of observations
    rownorm = @(xmat) sqrt(sum(xmat.^2, 2));

    % Problem: unique labels and how many there are
    kset = unique(lvec);
    k = length(kset);

    % Loop over all indexes and accumulate the DB score of each cluster
    % gi is the cluster centroid
    % mi is the mean distance from the centroid
    % Di contains the distance ratios between IX and each other cluster
    D = [];
    for ix = 1:k
        Xi = Xmat(lvec==kset(ix), :);
        gi = mean(Xi);
        mi = mean(rownorm(Xi - gi));
        Di = [];
        for jx = 1:k
            if jx~=ix
                Xj = Xmat(lvec==kset(jx), :);
                gj = mean(Xj);
                mj = mean(rownorm(Xj - gj));
                Di(end+1) = (mi + mj)/norm(gi - gj);
            end
        end
        D(end+1) = max(Di);
    end

    % DB score is the mean of the scores of the clusters
    score = mean(D);
end
