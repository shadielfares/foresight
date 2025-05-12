# Benefits of Neo4J

Though not part of the MVP, this will allow us to provide semantic and relevant feedback to the end-user.

Instead of just predicting what we the user will become based on current habits, we can provide feedback on what they can do
to reach an end-goal.

Here is a breakdown of what it provides:

```
| Feature              | Example                                                                |
| -------------------- | ---------------------------------------------------------------------- |
| Graph traversal      | Find all roles reachable from a given set of habits                    |
| Path queries         | "What’s the shortest path from current habits to 'ML Researcher'?"     |
| Community detection  | Discover clusters of roles with overlapping habits                     |
| Explainability       | Visual graph: *“You reached 'Entrepreneur' because of these 3 habits”* |
| Next-step suggestion | *“People with habits like yours often started networking next.”*       |
| Weighted edges       | Model strength of influence (e.g., `("Habit" → "Role", weight=0.8)`)   |

```