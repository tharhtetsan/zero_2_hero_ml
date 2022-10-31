# Title 

Please include your PR title in this format. 

```[Date]/[Version]/Summary of PR```

- Date: The date you want to make PR
- Version: The name of new version which is going to change
- Summary of PR: A short summary of your major changes

Example: 01-12-2021/ v0.0.7.2/ Cloud Logging and Request Format Validation 


# Description

Please include a summary of the change and which issue is fixed. Please also include relevant motivation and context. List any dependencies that are required for this change.

Example

- python logging and native cloud logging to log operation runtime and operation failures with INFO and WARNING LEVEL according to issue #81 [fixed/closed/resolved]

- validation method to show error response when user inputs incorrect response format according to issues #85 [fixed/closed/resolved]


## Type of change

Please delete options that are not relevant.

- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] This change requires a documentation update

# How Has This Been Tested?

Please describe the tests that you ran to verify your changes. Provide instructions so we can reproduce. Please also list any relevant details for your test configuration

- [ ] Test A (sheet link)
- [ ] Test B (sheet link)

**Test Configuration**:
* version: [The name of new version which is going to change]
* branch name: [dev/stg/prod]
* server:[cloud-run/prod/docker-locally/]

# Checklist:

Primary 
- [ ] **I have updated version number, docker port and uncomment EXPOSE 3000**
- [ ] **No need to update docker port and uncomment expose 3000**

Secondary 
- [ ] My code follows the style guidelines of this project
- [ ] I have performed a self-review of my own code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
