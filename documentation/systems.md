Basic Layout of Deployment Pipeline:
```mermaid
    graph TB;
        
        subgraph Development
            A[Dev Writes Code]
            B{Local Testing}
            C[Push to 'develop' Branch]
            C_2{Pull Request to Develop Branch}
            D{Remote testing}
            E[GitHub Action to deploy Triggered]
            
            A -- git commit --> B
            B -- Fail --> A
            B -- Pass --> C

            C --> D
            D -- Fail --> A
            D -- Pass --> C_2
            C_2 -- Code Review Pass --> E
            C_2 -- Code Review Fail --> A
        end
    
        subgraph Automatic Deployment to Dev Environment
            E --> F[Package Code for Deployment to Development Environment]
            F --> G[Upload Code to AWS development environment]
            G --> G_a[Automatic Code deployment with github pages]
        end
        
        subgraph Integration
            H{Perform Integration Tests}
            I{Perform User Testing}
            J{Human Approval}
            
            H -- Pass --> I
            H -- Fail --> A
            
            I -- Pass --> J
            I -- Fail --> A
        end
        
        G_a --> H
        J -- Pass --> K
        J -- Fail --> A
        subgraph Deploy to Production
            K[Initiate Pull Request from develop branch to master]
            L{Final Human Approval}
            M[Merge Develop Branch Into Master]
            O[Package Code for deployment to production environment]
            P[Upload Code to AWS Production Environment]
            
            L -- Pass --> M
            K --> L
            
            M --> O
            O --> P
            
            
        end
        
        L -- Fail --> A
        

```

# How to approve a Pull Request
Navigate to the "Pull Request" tab in github
![img.png](img.png)

change this drop down to the branch you want to pull into master, then click "create pull request"
![img_1.png](img_1.png)

write about how you're changing things:
![img_2.png](img_2.png)

let all the tests run
![img_3.png](img_3.png)

confirm the PR
![img_4.png](img_4.png)


# Basic Layout of Architecture (WIP):
