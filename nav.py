import pandas as pd

# NetflixNav – Data Exploration Script
# Author: Reiden Johnson
#
# This script performs exploratory analysis on the Netflix Titles
# dataset. The goal is to understand distribution patterns across
# countries, release years, genres, and actor appearances.
#
# Questions to Cover:
#   1. Countries that produce the most Netflix content
#   2. Average release year comparison between Movies and TV Shows
#   3. Most common genres on the platform
#   4. Number of titles featuring a selected actor (Adam Sandler)
#
# This file is designed to be a basic, transparent example of
# real-world dataset exploration using Python and Pandas!
# -------------------------------------------------------------------


# --------------------------------------------------------------
# Load Dataset
# --------------------------------------------------------------
print("Loading dataset...")
df = pd.read_csv("netflix_titles.csv")


# --------------------------------------------------------------
# Data Cleaning & Preparation
# --------------------------------------------------------------

# Country Cleanup:
# Some rows contain multiple comma-separated countries.
# We extract only the first for consistent aggregation.
df["country"] = df["country"].fillna("Unknown")
df["main_country"] = df["country"].apply(lambda x: x.split(",")[0].strip())

# Release Year:
df["release_year"] = df["release_year"].fillna(0)

# Genres:
df["listed_in"] = df["listed_in"].fillna("Unknown")

# Cast field (for Question 4):
df["cast"] = df["cast"].fillna("")


# --------------------------------------------------------------
# QUESTION 1:
# Which countries produce the most Netflix content?
# --------------------------------------------------------------
print("\n=====================================================")
print("1. Most Content by Country")
print("=====================================================")

country_counts = df["main_country"].value_counts()
top5_countries = country_counts.head(5)

print("\nTop 5 Content-Producing Countries:\n")
print(top5_countries)


# --------------------------------------------------------------
# QUESTION 2:
# What is the average release year for Movies vs TV Shows?
# --------------------------------------------------------------
print("\n=====================================================")
print("2. Average Release Year by Content Type")
print("=====================================================")

avg_release_year = (
    df.groupby("type")["release_year"]
      .mean()
      .round(2)
)

print("\nAverage Release Year:\n")
print(avg_release_year)


# --------------------------------------------------------------
# QUESTION 3:
# What are the top 10 most common genres on Netflix?
# --------------------------------------------------------------
print("\n=====================================================")
print("3. Most Common Genres")
print("=====================================================")

genre_series = (
    df["listed_in"]
      .str.split(",")
      .explode()
      .str.strip()
)

top_genres = genre_series.value_counts().head(10)

print("\nTop 10 Genres on Netflix:\n")
print(top_genres)


# --------------------------------------------------------------
# QUESTION 4:
# How many Netflix titles feature Adam Sandler?
# --------------------------------------------------------------
print("\n=====================================================")
print("4. Titles Featuring Adam Sandler")
print("=====================================================")

sandler_titles = df[df["cast"].str.contains("Adam Sandler", case=False, na=False)]

print(f"\nNumber of titles featuring Adam Sandler: {len(sandler_titles)}\n")

print("Titles featuring Adam Sandler:\n")
print(sandler_titles["title"].to_string(index=False))


# --------------------------------------------------------------
# End of Analysis
# --------------------------------------------------------------
print("\n=====================================================")
print("Analysis Complete")
print("=====================================================")

print("\nSummary of Outputs:")
print("✔ Country distribution analysis")
print("✔ Release year comparison")
print("✔ Genre frequency breakdown")
print("✔ Actor-specific filtering (Adam Sandler)\n")
