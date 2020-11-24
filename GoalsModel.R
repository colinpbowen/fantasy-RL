install.packages("extraDistr")
require(extraDistr)

goals <- rep(0,38)

for (i in 1:38) {
  
  shots_pg_range <- 2
  probs <- rep(1, shots_pg_range)/shots_pg_range
  n <- rcat(1, probs) - 1
  p <- runif(1, .05, .15)
  
  goals[i] <- rbinom(1, n,p)
}
