WITH daily AS (
  SELECT
    date,
    impressions,
    LAG(impressions) OVER (ORDER BY date) AS prev_day
  FROM ad_stats
)
SELECT
  date,
  impressions,
  prev_day,
  impressions - prev_day AS delta
FROM daily
WHERE ABS(impressions - prev_day) > 50000;
