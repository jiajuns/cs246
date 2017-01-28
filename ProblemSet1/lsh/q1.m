close all;clc


%% prepare data
load patches;
T1=lsh('lsh',10,24,size(patches,1),patches,'range',255);


%% part 1
tic;
for col = 100:100:1000
    [nnlsh, numcand] = lshlookup(patches(:,col), patches, T1, 'k', 4, 'distfun', 'lpnorm', 'distargs', {1});
end
toc

tic
for col = 100:100:1000
    d=sum(abs(bsxfun(@minus,patches(:,col),patches)));
    [ignore,ind]=sort(d);
end
toc

%% part 2 L

% error value for L
K = 24;
error = zeros(1, size(10:2:20, 2));
for L = 10:2:20
    T=lsh('lsh',L,K,size(patches,1),patches,'range',255);
    e = 0;
    for col = 100:100:1000
        [nnlsh, numcand] = lshlookup(patches(:,col), patches, T, 'k', 4, 'distfun', 'lpnorm', 'distargs', {1});
        d=sum(abs(bsxfun(@minus,patches(:,col),patches)));
        [ignore,ind]=sort(d);
        num = size(nnlsh, 2) - 1;
        size(nnlsh, 2)
        if num > 0
            LSH_dist = 0;
            linear_dist = 0;
            for i = 1:num
                LSH_dist = LSH_dist + lpnorm(patches(:, nnlsh(1+i)), patches(:, col));
                linear_dist = linear_dist + lpnorm(patches(:, ind(1+i)), patches(:, col));
            end
            e = e + LSH_dist/linear_dist;
        else
            e = e + 0;
        end
    end
    (L-10)/2+1
    error(1,(L-10)/2+1) = e/10;
end
figure(1);clf;
plot(10:2:20, error)
xlabel('L')
ylabel('error')
print('-dpng','-r300','-painters','L_error')

%% part 2 K
L = 10;
error = zeros(1, size(16:2:24, 2));
for K = 16:2:24
    T=lsh('lsh',L,K,size(patches,1),patches,'range',255);
    e = 0;
    for col = 100:100:1000
        [nnlsh, numcand] = lshlookup(patches(:,col), patches, T, 'k', 4, 'distfun', 'lpnorm', 'distargs', {1});
        d=sum(abs(bsxfun(@minus,patches(:,col),patches)));
        [ignore,ind]=sort(d);
        num = size(nnlsh, 2) - 1;
        size(nnlsh, 2)
        if num > 0
            LSH_dist = 0;
            linear_dist = 0;
            for i = 1:num
                LSH_dist = LSH_dist + lpnorm(patches(:, nnlsh(1+i)), patches(:, col));
                linear_dist = linear_dist + lpnorm(patches(:, ind(1+i)), patches(:, col));
            end
            e = e + LSH_dist/linear_dist;
        else
            e = e + 0;
        end
    end
    error(1,(K-16)/2+1) = e/10;
end
figure(2);clf;
plot(16:2:24, error)
xlabel('K')
ylabel('error')
print('-dpng','-r300','-painters','K_error')

%% part 3
T1=lsh('lsh',10,24,size(patches,1),patches,'range',255);

col = 100;
[nnlsh, numcand] = lshlookup(patches(:,col), patches, T1, 'k', 11, 'distfun', 'lpnorm', 'distargs', {1});
d=sum(abs(bsxfun(@minus,patches(:,col),patches)));
[ignore,ind]=sort(d);

figure(3);clf;
subplot(3,5,3)
imagesc(reshape(patches(:,ind(1)),20,20)); 
colormap gray;
axis image;
for k=1:10
    subplot(3,5,5+k)
    imagesc(reshape(patches(:,nnlsh(k+1)),20,20)); 
    colormap gray;
    axis image; 
end
print('-dpng','-r300','-painters','LSH_negihbor')


figure(4);clf;
subplot(3,5,3)
imagesc(reshape(patches(:,ind(1)),20,20)); 
colormap gray;
axis image;
for k=1:10
    subplot(3,5,5+k)
    imagesc(reshape(patches(:,ind(k+1)),20,20)); 
    colormap gray;
    axis image; 
end
print('-dpng','-r300','-painters','linear_negihbor')
