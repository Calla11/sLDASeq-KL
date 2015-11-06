function r = drchrnd(a,n)
p = length(a);
repmatData = repmat(a,n,1);
rtry = gamrnd(repmatData,1);
r = gamrnd(repmatData,1,[n,p]);
r = r ./ repmat(sum(r,2),1,p);

end

