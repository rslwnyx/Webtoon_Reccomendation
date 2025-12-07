Ypu can test the Reccomender bu using:
https://webtoonrecapp-tkbzkt2w3etnze6y7stqze.streamlit.app/


Webtoon Recommendation System - Project Report
1) Problem Definition Users struggle to find personalized content due to popularity-biased lists. The goal is to build a system that suggests webtoons based on content similarity, genre, and quality, enabling niche discovery.

2) Baseline Process & Score Started with Cosine Similarity on raw data. It failed due to the "Scale Problem"; high magnitude numbers (popularity) overpowered binary genre tags, resulting in irrelevant recommendations.

3) Feature Engineering & Results To fix the scale issue, I applied:

Log Transformation: on popularity.

MinMax Scaling: Normalized all numerical features to 0-1 range.

Feature Weighting: Prioritized Genre (x3.0) over Quality (x1.5).

Result: The model successfully balanced genre relevance with content quality.

4) Validation Scheme Used Sanity Checks (Qualitative Evaluation) on well-known titles (e.g., Tower of God). Since this is an unsupervised learning project without ground truth data, manual verification of relevance was the most effective method.

5) Final Pipeline Strategy Chose a "Hybrid Weighted Content Filtering" strategy. I combined normalized numerical stats (Score/Popularity) with weighted categorical data (Genres) to ensure recommendations are both high-quality and thematically similar.

6) Final Model vs. Baseline

Baseline: Recommended completely unrelated genres just because they were popular (e.g., Romance for Action fans).

Final Model: Provides contextually accurate recommendations (e.g., Solo Leveling correctly maps to other Action/Fantasy hits).

7) Business Alignment Yes. The model drives User Retention by surfacing high-quality, relevant series, encouraging users to spend more time on the platform instead of churning due to "bad" recommendations.

8) Deployment & Monitoring Deployed on Streamlit Cloud. Future success metrics include:

CTR (Click-Through Rate): Do users click suggestions?

Conversion Rate: Do they start reading?

Diversity: Does the model suggest varied content?

