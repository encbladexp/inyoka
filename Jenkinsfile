#!/usr/bin/env groovy

def runTestOnDatabase(String database) {
  sh """
  ${activate_venv}
  coverage run --branch manage.py test --setting tests.settings.${database} --testrunner='xmlrunner.extra.djangotestrunner.XMLTestRunner' || true
  coverage xml
  """
}

pipeline {
  agent { label 'inyoka-slave' }
  options {
    buildDiscarder(logRotator(numToKeepStr: '10'))
  }
  stages {
    stage('Prepare build') {
      parallel {
        stage('Build Virtualenv') {
          steps {
            script {
              requirementshash = sh returnStdout: true,
                                    script: "cat extra/requirements/development.txt extra/requirements/production.txt | sha256sum | awk '{print \$1}'"
              requirementshash = requirementshash.trim()
              venv_path = "~/venvs/${requirementshash}"
              activate_venv = ". ${venv_path}/bin/activate"
            }

            sh """
            if [ ! -d ${venv_path} ]
            then
              virtualenv ${venv_path}
              ${activate_venv}
              pip install unittest-xml-reporting
              pip install -r extra/requirements/development.txt
            fi
            """
          }
        }
        stage('Theme checkout') {
          steps {
            dir('theme-ubuntuusers') {
              git branch: 'staging', url: 'git@github.com:inyokaproject/theme-ubuntuusers'

              sh """
              git checkout ${env.BRANCH_NAME} || git checkout staging

              npm install
              ./node_modules/grunt-cli/bin/grunt
              """
            }
          }
        }
      }
    }
    stage('Link theme') {
      steps {
        dir('theme-ubuntuusers') {
          sh """
          ${activate_venv}
          python setup.py develop
          """
        }
      }
    }
    stage('Tests & Documentation') {
      parallel {
        stage('MySQL') {
          steps{
            runTestOnDatabase('mysql')
          }
        }
        stage('PostgreSQL') {
          steps{
            runTestOnDatabase('postgresql')
          }
        }
        stage('SQLite') {
          steps{
            runTestOnDatabase('sqlite')
          }
        }
        stage('Build Documentation') {
          when {
            branch 'staging'
          }
          steps {
            sh """
            ${activate_venv}
            head -n -21 example_development_settings.py > development_settings.py
            echo "SECRET_KEY = 'DEMO'" >> development_settings.py
            make -C docs html
            """

            publishHTML([allowMissing: false,
                         alwaysLinkToLastBuild: false,
                         keepAll: false,
                         reportDir: 'docs/build/html',
                         reportFiles: 'index.html',
                         reportName: 'Inyoka Documentation',
                         reportTitles: ''])
          }
        }
      }
    }
    stage('Analyse tests') {
      steps {
        junit 'sqlite.xml,mysql.xml,postgresql.xml'
        step([$class: 'CoberturaPublisher',
              autoUpdateHealth: false,
              autoUpdateStability: false,
              coberturaReportFile: 'coverage.xml',
              failUnhealthy: false,
              failUnstable: false,
              maxNumberOfBuilds: 0,
              onlyStable: false,
              sourceEncoding: 'ASCII',
              zoomCoverageChart: false])
      }
    }
  }
}
