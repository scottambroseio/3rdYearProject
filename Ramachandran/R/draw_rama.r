png('out_0.png')

scatter.data <- read.table("../tsv/out_0.tsv", header=FALSE, comment.char="", row.names=1, colClasses=c("character","numeric","numeric","factor"), col.names=c("name","phi","psi","type"))
scatter.psi <- scatter.data[which(scatter.data[,"type"]=="General"),"psi"]
scatter.phi <- scatter.data[which(scatter.data[,"type"]=="General"),"phi"]
par(pty="s")
plot(x=scatter.phi, y=scatter.psi, xlim=c(-180,180), ylim=c(-180,180), main="General", pch=20, xlab=expression(phi), ylab=expression(psi), cex=0.1, asp=1.0)

dev.off()

png('out_1.png')

scatter.data <- read.table("../tsv/out_1.tsv", header=FALSE, comment.char="", row.names=1, colClasses=c("character","numeric","numeric","factor"), col.names=c("name","phi","psi","type"))
scatter.psi <- scatter.data[which(scatter.data[,"type"]=="General"),"psi"]
scatter.phi <- scatter.data[which(scatter.data[,"type"]=="General"),"phi"]
par(pty="s")
plot(x=scatter.phi, y=scatter.psi, xlim=c(-180,180), ylim=c(-180,180), main="General", pch=20, xlab=expression(phi), ylab=expression(psi), cex=0.1, asp=1.0)

dev.off()

png('out_2.png')

scatter.data <- read.table("../tsv/out_2.tsv", header=FALSE, comment.char="", row.names=1, colClasses=c("character","numeric","numeric","factor"), col.names=c("name","phi","psi","type"))
scatter.psi <- scatter.data[which(scatter.data[,"type"]=="General"),"psi"]
scatter.phi <- scatter.data[which(scatter.data[,"type"]=="General"),"phi"]
par(pty="s")
plot(x=scatter.phi, y=scatter.psi, xlim=c(-180,180), ylim=c(-180,180), main="General", pch=20, xlab=expression(phi), ylab=expression(psi), cex=0.1, asp=1.0)

dev.off()

png('out_3.png')

scatter.data <- read.table("../tsv/out_3.tsv", header=FALSE, comment.char="", row.names=1, colClasses=c("character","numeric","numeric","factor"), col.names=c("name","phi","psi","type"))
scatter.psi <- scatter.data[which(scatter.data[,"type"]=="General"),"psi"]
scatter.phi <- scatter.data[which(scatter.data[,"type"]=="General"),"phi"]
par(pty="s")
plot(x=scatter.phi, y=scatter.psi, xlim=c(-180,180), ylim=c(-180,180), main="General", pch=20, xlab=expression(phi), ylab=expression(psi), cex=0.1, asp=1.0)

dev.off()

png('out_4.png')

scatter.data <- read.table("../tsv/out_4.tsv", header=FALSE, comment.char="", row.names=1, colClasses=c("character","numeric","numeric","factor"), col.names=c("name","phi","psi","type"))
scatter.psi <- scatter.data[which(scatter.data[,"type"]=="General"),"psi"]
scatter.phi <- scatter.data[which(scatter.data[,"type"]=="General"),"phi"]
par(pty="s")
plot(x=scatter.phi, y=scatter.psi, xlim=c(-180,180), ylim=c(-180,180), main="General", pch=20, xlab=expression(phi), ylab=expression(psi), cex=0.1, asp=1.0)

dev.off()

png('out_5.png')

scatter.data <- read.table("../tsv/out_5.tsv", header=FALSE, comment.char="", row.names=1, colClasses=c("character","numeric","numeric","factor"), col.names=c("name","phi","psi","type"))
scatter.psi <- scatter.data[which(scatter.data[,"type"]=="General"),"psi"]
scatter.phi <- scatter.data[which(scatter.data[,"type"]=="General"),"phi"]
par(pty="s")
plot(x=scatter.phi, y=scatter.psi, xlim=c(-180,180), ylim=c(-180,180), main="General", pch=20, xlab=expression(phi), ylab=expression(psi), cex=0.1, asp=1.0)

dev.off()

png('out_6.png')

scatter.data <- read.table("../tsv/out_6.tsv", header=FALSE, comment.char="", row.names=1, colClasses=c("character","numeric","numeric","factor"), col.names=c("name","phi","psi","type"))
scatter.psi <- scatter.data[which(scatter.data[,"type"]=="General"),"psi"]
scatter.phi <- scatter.data[which(scatter.data[,"type"]=="General"),"phi"]
par(pty="s")
plot(x=scatter.phi, y=scatter.psi, xlim=c(-180,180), ylim=c(-180,180), main="General", pch=20, xlab=expression(phi), ylab=expression(psi), cex=0.1, asp=1.0)

dev.off()

png('out_7.png')

scatter.data <- read.table("../tsv/out_7.tsv", header=FALSE, comment.char="", row.names=1, colClasses=c("character","numeric","numeric","factor"), col.names=c("name","phi","psi","type"))
scatter.psi <- scatter.data[which(scatter.data[,"type"]=="General"),"psi"]
scatter.phi <- scatter.data[which(scatter.data[,"type"]=="General"),"phi"]
par(pty="s")
plot(x=scatter.phi, y=scatter.psi, xlim=c(-180,180), ylim=c(-180,180), main="General", pch=20, xlab=expression(phi), ylab=expression(psi), cex=0.1, asp=1.0)

dev.off()

png('out_8.png')

scatter.data <- read.table("../tsv/out_8.tsv", header=FALSE, comment.char="", row.names=1, colClasses=c("character","numeric","numeric","factor"), col.names=c("name","phi","psi","type"))
scatter.psi <- scatter.data[which(scatter.data[,"type"]=="General"),"psi"]
scatter.phi <- scatter.data[which(scatter.data[,"type"]=="General"),"phi"]
par(pty="s")
plot(x=scatter.phi, y=scatter.psi, xlim=c(-180,180), ylim=c(-180,180), main="General", pch=20, xlab=expression(phi), ylab=expression(psi), cex=0.1, asp=1.0)

dev.off()

png('out_9.png')

scatter.data <- read.table("../tsv/out_9.tsv", header=FALSE, comment.char="", row.names=1, colClasses=c("character","numeric","numeric","factor"), col.names=c("name","phi","psi","type"))
scatter.psi <- scatter.data[which(scatter.data[,"type"]=="General"),"psi"]
scatter.phi <- scatter.data[which(scatter.data[,"type"]=="General"),"phi"]
par(pty="s")
plot(x=scatter.phi, y=scatter.psi, xlim=c(-180,180), ylim=c(-180,180), main="General", pch=20, xlab=expression(phi), ylab=expression(psi), cex=0.1, asp=1.0)

dev.off()

png('out_10.png')

scatter.data <- read.table("../tsv/out_10.tsv", header=FALSE, comment.char="", row.names=1, colClasses=c("character","numeric","numeric","factor"), col.names=c("name","phi","psi","type"))
scatter.psi <- scatter.data[which(scatter.data[,"type"]=="General"),"psi"]
scatter.phi <- scatter.data[which(scatter.data[,"type"]=="General"),"phi"]
par(pty="s")
plot(x=scatter.phi, y=scatter.psi, xlim=c(-180,180), ylim=c(-180,180), main="General", pch=20, xlab=expression(phi), ylab=expression(psi), cex=0.1, asp=1.0)

dev.off()

png('out_11.png')

scatter.data <- read.table("../tsv/out_11.tsv", header=FALSE, comment.char="", row.names=1, colClasses=c("character","numeric","numeric","factor"), col.names=c("name","phi","psi","type"))
scatter.psi <- scatter.data[which(scatter.data[,"type"]=="General"),"psi"]
scatter.phi <- scatter.data[which(scatter.data[,"type"]=="General"),"phi"]
par(pty="s")
plot(x=scatter.phi, y=scatter.psi, xlim=c(-180,180), ylim=c(-180,180), main="General", pch=20, xlab=expression(phi), ylab=expression(psi), cex=0.1, asp=1.0)

dev.off()