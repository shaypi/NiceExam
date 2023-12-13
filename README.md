# NiceExam

Welcome to NiceExam, a project designed for seamless deployment using GitHub Actions. This README provides an overview of the deployment process and the directory structure to help you get started.

## Getting Started

Before deploying NiceExam, ensure you have the necessary credentials and permissions set up for AWS and GitHub Actions.

## Deployment Process

The deployment process for the NiceExam project involves three GitHub Actions runners. Make sure to follow the specified order for a successful deployment:

1. [**primary.yml**](https://github.com/shaypi/NiceExam/actions/workflows/primary.yml): This runner creates the Infrastructure stack, Task Definition, and the ECS Service.

2. [**CI-Infra.yml**](https://github.com/shaypi/NiceExam/blob/main/.github/workflows/CI-Infra.yml): This runner handles the creation of CI Infrastructure stacks, including CodeCommit, CodeDeploy, CodePipeline, and CodeBuild.

3. [**codecommit.yml**](https://github.com/shaypi/NiceExam/blob/main/.github/workflows/codecommit.yml): This runner pushes the code from GitHub into the CodeCommit repository.

## Directory Structure

Ensure you deploy the project in the following order for a smooth deployment process:

1. **primary.yml**
2. **CI-Infra.yml**
3. **codecommit.yml**

```plaintext
.
|-- README.md
|-- app
|   |-- Dockerfile
|   |-- app.py
|   |-- requirements.txt
|   `-- templates
|       `-- index.html
|-- buildspec.yml
`-- cloudformation
    |-- cicd.yaml
    |-- infra.yaml
    `-- template2.yaml
```

Feel free to explore the project's directory structure for a better understanding of the components and configurations involved in NiceExam.