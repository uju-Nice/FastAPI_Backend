# FastAPI is used for building web APIs with python type hints and FastAPI dependencies are Pydantic and Starlette
starlette for web part  & pydantic for data part

python -m pip install --upgrade pip        .... To use the latest pip to install
python -m ensurepip --upgrade         ..... Incase of error not finding pip when upgrading
pip install "fastapi[standard]"       .... To create and ac tiavet virtual env for FastApi
fastapi dev main.py                    ...... Runs the server

CREATE A VIRTUAL ENVIRONEMNT or use uv instead (which also create virtual env and install other packages and dependenecies needed for your projects)

powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"    .... installs uv on window shell.

uv self update     ....... Updates uv

echo 'eval "$(uv generate-shell-completion bash)"' >> ~/.bashrc       .... Enables shell autocompletion for uv commands.


source .venv/bin/activate                   ...... To activate the virtual env 

Deploy your application to FastApi Cloud or Vercel AI
on the terminal type ...... 
fastapi login 
fastapi deploy 
