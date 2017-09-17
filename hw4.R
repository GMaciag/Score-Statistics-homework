setwd ("/Users/PATH/TO/DIRECTORY")
s100 <- unlist(read.table("100rand",head=F)) 
tmp <-table(s100)
counts <- as.vector(tmp)
C100 <- rev(cumsum(rev(counts)))/100
S100 <- as.numeric(names(tmp))
plot(S100, C100, main = NULL, xlab="score", ylab="Cummulative count", type="l",col="blue", log="y")
lambda <- log (2) /2.
evalue = function(x){1.0*200*1334377*exp(-lambda*x)}
curve(evalue, from=20, to=90, type="l",lwd=3, col="red", log="y", add=T)