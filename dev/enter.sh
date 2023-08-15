source env/bin/activate

export DEBUG="True"

if [ -z "$1" ] || [[ "test" == "$1"* ]]
then
	echo 'TEST DATABASE (partnership_system_test)'
	export DB_NAME="partnership_system_test"
    export DB_USER="dchako"
    export DB_PASSWORD="mypassword"
    export DB_PORT="3306"
    export DEBUG=True

	
	
elif [[ "prod" == "$1"* ]] || [[ "production" == "$1"* ]]
then
	echo 'PRODUCTION DATABASE (partnership_system_prod)'
	export DB_NAME="partnership_system_prod"
    export DB_USER="dchako"
    export DB_PASSWORD="mypassword"
    export DB_PORT="3306"
    export DEBUG=False
	
fi

export ROOT=`pwd`
export MANAGE="python $ROOT/manage.py"

alias m=$MANAGE