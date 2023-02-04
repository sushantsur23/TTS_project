echo [$(date)] : "CREATING API ENDPOINT !"
touch main.py

echo [$(date)] : "CREATING CONDA ENVIRONMENT"
conda create --prefix ./tts1 python=${_VERSION_} -y
source activate ./tts1

echo [$(date)] : "CREATE REQUIREMENTS TEXT FILE"
touch requirements.txt
pip_requirements() {
if test "$#" -eq 0
then 
  echo $'\nProvide at least one Python package name\n' 
else 
  for package in "$@"
  do
    pip install $package
    pip freeze | grep -i $package >> requirements.txt
  done
fi
}
pip_requirements numpy pandas seaborn sklearn pymongo fastapi notebook matplotlib ipykernel PyYAML notebook dill uvicorn
