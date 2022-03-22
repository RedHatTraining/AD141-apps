#!/usr/bin/env python3
reward_pts = {"Bryce": 500, "Heather": 2000, "Kaylie": 750}
points = reward_pts.get("Bryce")      # returns 500
print("Bryce:", points)
points = reward_pts.get("Stephanie")  # returns None
print("Stephanie:", points)

# Supplying a different value to return other than None
points = reward_pts.get("Stephanie", 0)  # returns 0
print("Stephanie:", points)
print("Current Dictionary Contents:", reward_pts)
