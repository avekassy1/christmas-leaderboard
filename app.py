import streamlit as st
from typing import List, Dict

# Define the structure of a quote
class Quote:
    def __init__(self, id: int, rank: int, quote: str, submitted_by: str, votes: int):
        self.id = id
        self.rank = rank
        self.quote = quote
        self.submitted_by = submitted_by
        self.votes = votes

# Initialize a list of mock quotes
mock_quotes: List[Quote] = [
    Quote(id=1, rank=1, quote="\"Melyik Magyarország?\" tette fel a kérdést nagyfater", submitted_by="Lili", votes=123),
    Quote(id=2, rank=2, quote="Szinte ez mar olyan mint a szocializmusba...?", submitted_by="Jeno", votes=98),
    Quote(id=3, rank=3, quote="Csak katonai akcio volt!", submitted_by="Istvan", votes=76),
]

# Sort quotes by votes
def sort_quotes(quotes: List[Quote]) -> List[Quote]:
    return sorted(quotes, key=lambda x: x.votes, reverse=True)

# Update the ranks after sorting
def update_ranks(quotes: List[Quote]):
    for idx, quote in enumerate(quotes):
        quote.rank = idx + 1

# Main App
st.title("🎄 Christmas Quote Leaderboard 🎄")

# Sidebar form to submit a new quote
with st.sidebar:
    st.header("Submit a Quote")
    new_quote = st.text_area("Quote", "")
    submitter = st.text_input("Submitted by", "")
    if st.button("Submit"):
        if new_quote and submitter:
            new_id = max(q.id for q in mock_quotes) + 1
            mock_quotes.append(Quote(id=new_id, rank=len(mock_quotes) + 1, quote=new_quote, submitted_by=submitter, votes=0))
            st.sidebar.success("Quote submitted!")
        else:
            st.sidebar.error("Please fill in both fields.")

# Display the leaderboard
st.subheader("Leaderboard")
sorted_quotes = sort_quotes(mock_quotes)
update_ranks(sorted_quotes)

for quote in sorted_quotes:
    st.write(f"### #{quote.rank} {quote.quote}")
    st.write(f"**Submitted by**: {quote.submitted_by}")
    st.write(f"❤️ **Votes**: {quote.votes}")

    # Voting button
    if st.button(f"Vote for #{quote.rank}", key=f"vote-{quote.id}"):
        quote.votes += 1
        st.experimental_rerun()  # Refresh to update votes dynamically
