### What is this, in short?

[This](https://t.me/sudokusatbot) telegram bot

### What is it for?

It solves [sudoku](https://en.wikipedia.org/wiki/Sudoku) puzzles like crazy

### How is it different from other bots?

Most of other bots use some kind of brute force algorithm.
They fail on some especially hard sudokus, like [this one](https://secure.i.telegraph.co.uk/multimedia/archive/02260/Untitled-1_2260717b.jpg)

This bot, however, translates sudoku to 
[SAT problem](https://en.wikipedia.org/wiki/Boolean_satisfiability_problem),
and then uses efficient SAT solving algorithm to solve it.

### What technology does it use?
It runs on [Amazon Cloud](https://aws.amazon.com/).

More specifically, it is two serverless AWS Lambda functions. 
One (_sudoku_) is an api for solving sudokus, 
another (_tgbot_) is just an adapter for telegram bot
to use this api.

### How do i deploy it to my Amazon Cloud?

1. Install [sam cli interface](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)
2. Don't forget to set up iam credentials
3. Go to repo folder, run `sam build --use-container`, then `sam deploy --guided`
4. For telegram bot microservice, set up 
environmental variables in aws web interface: `BOT_TOKEN` is a token of your bot, 
`SUDOKU_API_URL` is the url of _sudoku_ web app 
(probably something like `https://{id}.execute-api.{location}.amazonaws.com/Prod/solve`)
 
