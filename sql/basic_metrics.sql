SELECT
  date,
  SUM(impressions) AS total_impressions,
  SUM(clicks) AS total_clicks,
  SUM(conversions) AS total_conversions,
  ROUND(SUM(clicks)::decimal / NULLIF(SUM(impressions), 0), 4) AS CTR,
  ROUND(SUM(spend)::decimal / NULLIF(SUM(clicks), 0), 2) AS CPC
FROM ad_stats
GROUP BY date
ORDER BY date;
