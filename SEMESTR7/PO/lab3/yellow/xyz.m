dirOutput = dir (fullfile('C:\Users\adm\Desktop\yellow\*.jpg'));
fileName={dirOutput.name};
n=size(fileName,2);
for i=1:n
    a=imread(fileName{i});
    figure, imshow(a)
end