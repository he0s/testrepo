pipeline {
  agent {
    kubernetes {
      yaml """
      metadata:
        labels:
          component: test-repo
      spec:
        containers:
        - name: jnlp
          imagePullPolicy: Always
          env:
          - name: CONTAINER_ENV_VAR
            value: jnlp
          - name: POD_IP
            valueFrom:
              fieldRef:
                fieldPath: status.podIP
          - name: DOCKER_HOST
            value: tcp://localhost:2375
        - name: python
          image: python:latest
          command:
          - cat
          tty: true
        - name: dind
          image: docker:dind
          securityContext:
            privileged: true
          volumeMounts:
            - name: dind-storage
              mountPath: /var/lib/docker
        volumes:
          - name: dind-storage
            emptyDir: {}
      """
    }
  }
    options {
      timeout(time: 1, unit: 'HOURS')
    }
    environment {
      image_name = "python"
    }
    triggers {
      githubPush()
    }
    stages {
      stage('syntax-check') {
        steps {
          container('python') {
            script {
              sh "python --version"
            }
          }
        }
      }
    }
    // post {
    //   failure {
    //     slackSend (color: '#FF0000', message: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})")
    //   }
    // }
}
