Environment

This is about isolating project dependencies.
- Imagine Project A needs: FastAPI 1.x
- while Project B needs: FastAPI 2.x
- Installing everything globally can cause conflicts.

That's why Python uses virtual environments.

- Create One:
python -m venv .venv

Activate virtual environment:
.venv\Scripts\activate

You'll see something like:
(.venv) C:\projects\myapp>

Now:
pip install requests
- This package goes into that environment