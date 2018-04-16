method1 <- c(12.0129, 12.0072, 12.0064, 12.0054, 12.0016,
             11.9853, 11.9949, 11.9985, 12.0077, 12.0061)

method2 <- c(12.0318, 12.0246, 12.0069, 12.0006, 12.0075)
alpha=.05
t.test(method1, method2, var.equal=FALSE, alternative="two.sided", conf.level=1-alpha)
t.test(method1, method2, var.equal=TRUE, alternative="two.sided", conf.level=1-alpha)
