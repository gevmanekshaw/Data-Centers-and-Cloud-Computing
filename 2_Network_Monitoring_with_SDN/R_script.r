statis <- read.csv(file="C:/Users/user/stats.csv", header = FALSE )
colnames(statis) <- c("datapath","port","rx_by", "tx_by")
statis1 <- subset(statis, statis[ , 2] != 65534)
statis2 <- subset(statis1, statis1[ , "datapath"] != 3)
Link1 <- subset(statis2, statis2[ , "datapath"] == 1 )
Link1 <- subset(Link1, Link1[ , "port"] == 1 )
Link2 <- subset(statis2, statis2[ , "datapath"] == 1 )
Link2 <- subset(Link2, Link2[ , "port"] == 2 )
Link3 <- subset(statis2, statis2[ , "datapath"] == 2 )
Link3 <- subset(Link3, Link3[ , "port"] == 2 )

for(x in 1:nrow(smple2))
     Link1[x,5] <- sum(Link1[x,3], Link1[x,4])

SLink1 <- Link1
SLink2 <- Link2
SLink3 <- Link3
for(x in 1:nrow(Link1))
     SLink1[x,5] <- sum(SLink1[x,3], SLink1[x,4])
for(x in 1:nrow(SLink2))
     SLink2[x,5] <- sum(SLink2[x,3], SLink2[x,4])
for(x in 1:nrow(SLink3))
     SLink3[x,5] <- sum(SLink3[x,3], SLink3[x,4])

for(x in 1:nrow(SLink1))
     SLink1[x,6] <- ( SLink1[(x+1),5] - SLink1[x,5] )
for(x in 1:nrow(SLink1))
     SLink1[x,7] <- ( SLink1[(x),6]/300 )
for(x in 1:nrow(SLink1))
     SLink1[x,8] <- ( SLink1[(x),7]*8 )
View(SLink1)
colnames(SLink1) <- c("datapath","port","rx_by", "tx_by","tot_by", "by_diff", "by/sec", "bits/sec")
for(x in 1:nrow(SLink2))
     SLink2[x,6] <- ( SLink2[(x+1),5] - SLink2[x,5] )
for(x in 1:nrow(SLink2))
     SLink2[x,7] <- ( SLink2[(x),6]/300 )
for(x in 1:nrow(SLink2))
     SLink2[x,8] <- ( SLink2[(x),7]*8 )
colnames(SLink2) <- c("datapath","port","rx_by", "tx_by","tot_by", "by_diff", "by/sec", "bits/sec")

for(x in 1:nrow(SLink3))
     SLink3[x,6] <- ( SLink3[(x+1),5] - SLink3[x,5] )
for(x in 1:nrow(SLink3))
     SLink3[x,7] <- ( SLink3[(x),6]/300 )
for(x in 1:nrow(SLink3))
     SLink3[x,8] <- ( SLink3[(x),7]*8 )


colnames(SLink3) <- c("datapath","port","rx_by", "tx_by","tot_by", "by_diff", "by/sec", "bits/sec")


for(x in 1:(nrow(SLink1)-1))
     SLink1[x,9] <- x
for(x in 1:(nrow(SLink2)-1))
     SLink2[x,9] <- x
for(x in 1:(nrow(SLink3)-1))
     SLink3[x,9] <- x
plot(SLink1$time, SLink1$bitspsec)
plot(SLink2$time, SLink2$bitspsec)
plot(SLink3$time, SLink3$bitspsec)

