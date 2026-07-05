---
title: Event Horizon — How Artificial Spotify Streams Broke A Kalshi Market
type: source
tags: [source, event-horizon, kalshi, settlement, culture-markets, cross-wiki]
keywords: [spotify, stream-botting, kalshi, oracle, manipulation]
related:
  - concepts/kalshi-spotify-oracle-manipulation-2026-07.md
  - entities/platforms/kalshi.md
  - concepts/prediction-markets-crossover.md
  - sources/arxiv-2606.31675-settlement-manipulation-prediction-markets-2026-07-01.md
  - osint-wiki/sources/substack-rss-event-horizon-2026-07-03-how-artificial-spotify-streams-broke-a-kalshi-ma.md
maturity: validated
created: 2026-07-05
updated: 2026-07-05
read_status: deep-read
cross-wiki-source: @osint-wiki/sources/substack-rss-event-horizon-2026-07-03-how-artificial-spotify-streams-broke-a-kalshi-ma.md
---

# Event Horizon — How Artificial Spotify Streams Broke A Kalshi Market

## Relations

- @concepts/kalshi-spotify-oracle-manipulation-2026-07.md — synthesized concept
- @osint-wiki/sources/substack-rss-event-horizon-2026-07-03-how-artificial-spotify-streams-broke-a-kalshi-ma.md  (cross-wiki source)

## Raw Concept

Guest column Caleb Davies (GaetenD), Event Horizon 2026-07-03. **Location:** `cemini-egress-fi:/opt/cemini-bulk/research/osint/substack-rss-event-horizon-2026-07-03-how-artificial-spotify-streams-broke-a-kalshi-ma.md`

## Narrative

Primary source for `@concepts/kalshi-spotify-oracle-manipulation-2026-07.md`. Full body below (RSS capture).

Guest column:  Caleb Davies, known on Twitter and Kalshi as  GaetenD , is a long-time prediction markets trader currently ranked fifth in lifetime earnings on culture markets on Kalshi.

 When trading in Spotify prediction markets, there are a ton of variables that you need to consider: day of the week, genre, days since release, new releases, and prior weeks’ performance. Now there’s a new one: Somebody appears to have manipulated streams in a way that benefited prediction-market positions.

 Botting on Spotify

 Stream botting is artificially inflating a song’s play count using automated tools rather than real listeners. The methods range from simple scripts running on a loop to sophisticated stream farms to malware that infects devices and streams the songs. The goal is to make fake plays look real. The more the streaming resembles actual listener behavior, the harder it is to detect.

 Spotify isn’t oblivious to this. They conduct audits, remove suspicious streams, and have pulled royalty payments from artists caught botting. The audits are done daily before each chart is published, a little more thoroughly at the beginning of each month, and one final, very thorough review is done before Spotify Wrapped is released at the end of each year. But identifying botted streams is an imperfect art and not all are caught quickly, if at all.

 People do it for a few reasons. The most obvious is royalties: Spotify pays out per stream, and if your bots are convincing enough to survive an audit, you can make a haul from your shitty songs. Labels and smaller artists have used it for years to juice chart positions, manufacture the appearance of momentum, or hit thresholds that trigger algorithmic playlist placement. Get on Discover Weekly or New Music Friday and the fake streams pay for themselves many times over.

 But what if instead of needing to play the long game of playlisting, royalty collection, and building popularity, you could just 100x your money in a day? And that you could pull it off without any risk of Spotify blacklisting you? That’s where prediction markets come in. And there is strong evidence that someone has already found this one neat trick (traders hate it!).

 Examining the evidence

 Spotify makes daily stream histories available globally and by country  here . Every morning, I put on my slippers, grab the  WSJ  from the porch, pour a glass of bourbon, then download the day’s US and global Spotify data and update my projections.

 When you do this every day (the Spotify part, not the rest of it), you notice when things are off. The charts are a dance of day-of-week trends, new songs and their rapid decays, the long-term decay of established songs, and the occasional viral hit. When something spikes outside of that framework, it warrants a closer look.

 There are several things I look for if I suspect fraudulent streams:

    Geographic targeting  – Is the surge in streams in a single country or worldwide? If it’s widespread, it is less likely to be artificial. A botted stream that doesn’t impact the targeted country’s chart is a wasted one.

    Impact on the rest of the artist’s catalog  – Some events are song-specific (a music video release, a song catching fire on TikTok), but others like concerts, television appearances, or a biopic release lift the entire catalog. If only a single track is impacted, it is more suspicious than if the entire catalog is.

    Suddenness of the trend  – Viral hits tend to build up over time rather than jumping up the charts in a single day. Likewise, their declines tend to be gradual rather than sudden. If a spike lasts a single day or a handful of days then drops again suddenly, that’s suspicious, too.

    Violation of day-of-week patterns  – Fridays are the strongest streaming days. Sundays are by far the weakest. The rest of the days are roughly even. Saturday to Sunday increases are rare. Anything outside of these norms raises flags.

   Applying your knowledge

 Now that you know how to detect fraud, I’m going to put you to the test.

 Click on this chart. It shows the US/global ratio for every song that charted on both charts during the time period. The grayed-out lines are within a normal range. The highlighted lines show some very unusual activity. We can see that the US-to-global ratio skyrockets for several Bad Bunny songs on Monday, February 2 and again on Sunday, February 8. It also has a big jump for “Opalite” by Taylor Swift on Friday.

               What do you think? Any reason to suspect fraud here?

 Of course not! That data is exactly what we’d expect. Bad Bunny won Album of the Year at the Grammys and his catalog got a boost. Taylor Swift dropped a video for “Opalite” that was initially available only on Spotify Premium and Apple Music, before later being released on YouTube, so it makes sense that would spike her US/global ratio. And you can see that the curves are smooth. No reason to suspect manipulation here.

 If you got that right, pat yourself on the head. If you didn’t, you’re really bad at this. I labeled the damn thing for you! Now click on this one. It again shows the US/global ratio for every song on both US and global for the date range.

                                       Anything suspicious here?

 I hope you said “Yes.” This is about as blatant as it gets. This is a streams boost targeted exclusively at the US that violates the normal day-of-week flow in a very sudden way. And this chart actually understates the severity because it uses filtered streams. On unfiltered streams, the cheating is ALS-ice-bucket-over-the-head-while-getting-kicked-in-the-nuts obvious:

               I had to expand the y-axis from 150 to 400 to fit these lines into it! On Tuesday, there were more botted streams removed from the US than there were legitimate streams in the rest of the world for “Janice STFU.”

 The Malcolm Todd case

 On June 22, there was about $2k in open interest in the Malcolm Todd bracket and the share prices were in the single digits. Because his song “Earrings” had been stable for a while 500k+ streams below the chart leaders, if anything, being in the single digits rather than $0.01 was generous to its chances. Over the course of the week, open interest increased to about $76k, which is a lot for a dead bracket. Most of the dead brackets were in the low thousands in open interest. Somebody accumulated a lot of shares that were extremely likely to become worthless on the morning of July 1.

 On Tuesday, June 30, Spotify market enjoyers of all shapes and sizes rolled out of bed, grabbed their  WSJ s, and poured their own bourbon while anxiously awaiting the results. All eyes were on Drake and Olivia Dean. Would Spotify be able to stop this dubious plan from working?

 They did! The results were delayed for hours, and when they were posted, traders breathed a sigh of relief as the top US song was not “Janice STFU” or “Man I Need.” No, it was Malcolm Todd’s “Earrings.” Wait…what? How the f……? Those shares were worthless, but now they became worth $1 each? A previously stable song at 500k+ streams below the leader won? To illustrate how unlikely that was, here is every Sunday to Monday gain for “Earrings” since it emerged on the charts:

                                       This isn’t just an unlikely result, it’s as close to a mathematical impossibility as you can get. If you and I both chose a star at random from all the stars in the observable universe, the odds that we chose the same one would be 77,000 times as likely as this increase occurring by chance. (Nerds: The same day-of-week comparisons of streaming changes for a stable song are close to a normal distribution. This result was an 11.24 sigma outcome.) Spotify was so busy filtering out artificial “Janice” and “Man I Need” streams that they missed Malcolm Todd’s artificial surge, which you can see in the earlier graphs as well.

 On July 1, Spotify removed the artificial streams, but by then it was too late for Kalshi traders* because the market had already been paid out. Spotify’s auditing process was sufficient for Spotify’s purposes, but too slow to prevent a Kalshi market from being paid out based on artificial streams.

  (* Polymarket did not have a Malcolm Todd “Earrings” bracket, so no Polymarket trader profited from this specific fraud. However, their daily markets remain fundamentally exposed to the exact same structural exploit.)

 The fate of Spotify markets

 As much as it pains me (and my wallet) to say: Spotify daily and monthly markets are fundamentally broken. I’ll walk through why.

    The cost of manipulating the resolution source is small compared to the potential profits  – It simply doesn’t cost very much to bot streams. There are a ton of websites that can easily be found on Google that offer those exact services.

    The odds of getting caught are very low  – Short of a full audit of a trader’s financial statements, linking a specific trader to a botting effort is extremely difficult. Even if a single trader owns all the shares of a winning fraudulent bracket, how do you prove they are the person who manipulated the results? A sophisticated fraudster could have somebody else do the botting, making it even more difficult to pin on them.

    There are few obvious consequences for failing  – Unlike an artist or a label that boosts their own songs, a prediction market trader receives no compensation from Spotify itself, so Spotify has no way of holding them accountable for the likely fraudulent streams. Spotify just removes the streams and the fraudster is only out the cost of them. They have no risk of losing royalties or being delisted.

    Spotify’s internal controls aren’t calibrated for prediction markets  – Spotify’s cadence of daily, monthly, and annual clean-up efforts work just fine for Spotify. By their end-of-the-year Spotify Wrapped, their data is as clean as it will get. But that’s not good enough for prediction markets, which pay out daily. Fraudsters can get rewarded immediately even if Spotify later catches and removes their streams.

   Broader implications

 Let me lay out an example I totally made up on my own and didn’t steal from anywhere:

 A nuclear power plant dumps its waste into a river. Because of the toxicity of the river, the fish grow a third eye and taste terrible, ruining the lives of all fishermen who depend on the river. Those fishermen have a legal recourse through the Clean Water Act. They can hold the nuclear power plant liable for the pollution. Our legal system can handle this case.

 But what if, instead of the nuclear power plant dumping its waste into a river, a prediction market platform creates a market on whether the river will be closed for contamination at any point this year? This creates a financial incentive for traders to contaminate the river and, if they do, it is not obvious under the current legal framework how the prediction market platform that created that incentive would be held liable.

 This concept applies to the Spotify markets listed on Kalshi and Polymarket. Those markets provide an incentive for traders to manipulate stream counts, which means that Spotify has to dedicate more resources to their audits through no fault of their own. Yet because no Clean Water Act-type framework is in place for prediction markets, Spotify does not have an obvious legal recourse against the prediction market platforms even though their negative externalities cause Spotify harm.

 Recommendations

 Kalshi paid out a market based on incorrect results over calls for a delay in payment while an investigation was performed. (To be clear, Kalshi is investigating the situation, and  The Event Horizon  is aware that Kalshi is in contact with Spotify.) Regulators have fallen behind the industry and need to catch up. I have recommendations for each on how to move forward.

 Before the June 29 results posted, I personally warned Kalshi about the potential for
