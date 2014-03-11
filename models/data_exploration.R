x <- read.table('/Users/kperko/code/kaggles/kaggle-walmart/data/stores.csv', sep=',', h=T)
summary(x)
str(x)
plot(x)
head(x)

#merge the stores, test and train dataset
#perform 5-fold CV so we're okay merging these
#merge the features dataset on the week