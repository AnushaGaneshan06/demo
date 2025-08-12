@echo off
REM Push to GitHub
git add .
git commit -m "Updated code"
git push origin main

REM Store push info in MongoDB using Python
python store_in_mongo.py

pause

