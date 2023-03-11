# Databricks notebook source
# MAGIC %md 
# MAGIC 
# MAGIC <img src='https://github.com/databricks-industry-solutions/.github/raw/main/profile/solacc_logo_wide.png' width="1000" ></img>
# MAGIC # How to Contribute - The Field Guide
# MAGIC 
# MAGIC Thank you for your interest in contributing to solution accelerators! Solution accelerator are Databricks' repository to host reusable technical assets for common industry technical patterns and use case solutions. The program is run by Sales GTM Verticals and supported by field contribution.
# MAGIC 
# MAGIC The purpose of this notebook is to describe the process for contributing to accelerators and provide helpful checklists for important milestones.
# MAGIC <img src='https://github.com/databricks-industry-solutions/.github/raw/main/profile/Solution%20Accelerator%20FY24.jpg'></img>
# MAGIC 
# MAGIC Maintainer: [@nicole.lu](https://databricks.enterprise.slack.com/team/jingting_lu)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Initialization & Intake: Before spending any time contributing to an accelerator
# MAGIC ❓ If you brought your own code, can you summarize what problem your code solves in less than 100 words?
# MAGIC 
# MAGIC ❓  Have you discussed the topic with a Technical Director? If you are not sure which vertical your work is best suited for, contact [@nicole.lu](https://databricks.enterprise.slack.com/team/jingting_lu) for an intake consultation. The Technical Directors are:
# MAGIC   * Retail CPG: Bryan Smith 
# MAGIC   * Financial Services: Antoine Amend, Eon Retief
# MAGIC   * Media Entertainment: Dan Morris
# MAGIC   * Health Life Sciense: Amir Kermany, Aaron Zarova
# MAGIC   * Manufacturing: Bala Amavasai
# MAGIC   * Cyber Security: Lipyeow Lim
# MAGIC   
# MAGIC   
# MAGIC 
# MAGIC 
# MAGIC ❓  Do you know the scope of work for this accelerator? 
# MAGIC   * You may need to provide code and optionally a blog post, video recording or slides. 
# MAGIC 
# MAGIC   * The technical director will discuss and decide which **publishing tier** the accelerator will be launched at. The **publishing tier** determines the full scope and the list of final deliverables for the accelerator. The most basic tier requires a repo. Higher tiers may require a blog post, video recording and more. 
# MAGIC   * The industry vertical will lean in with marketing resources if they decide to publish the accelerator at a higher tier 💪
# MAGIC 
# MAGIC ❓  Have you received a repo for the accelerator and gained write access to your repo in https://github.com/databricks-industry-solutions?
# MAGIC <img src='https://raw.githubusercontent.com/databricks-industry-solutions/.github/main/profile/Solution%20Accelerator%20FY24%20(1).jpg'></img>

# COMMAND ----------

# MAGIC %md 
# MAGIC ## Commit: Before Making Your First Commit
# MAGIC ❓ Is the code reusable by a broad array of customers? No customer-specific implementation details please.
# MAGIC 
# MAGIC ❓ Does the code contain any credentials? If yes, **scrub** the credentials from your code. Contact [@nicole.lu](https://databricks.enterprise.slack.com/team/jingting_lu) to set up secrets in demo and testing workspaces. Also prepare a short paragraph describing how the user would set up the dependencies and collect their own credentials 
# MAGIC 
# MAGIC ❓ Do we have the rights to use the source datasets and libraries in your code?
# MAGIC - Please fill out the dependency-license table in the README. Make sure our dependencies are open source. If we need to use some written documentation to substantiate our rights to use anything, file a legal review ticket 
# MAGIC - If you need to synthesize and store some source data, use a publically accessible cloud storage, such as `s3://db-gtm-industry-solutions/data/`
# MAGIC 
# MAGIC ❓ Have you explored https://github.com/databricks-industry-solutions/industry-solutions-blueprints? This repo illustrates a compulsory directory standard. All new accelerator repos are created based on this template
# MAGIC 
# MAGIC - **Narrative notebooks** are stored on the top level and **numbered**. 
# MAGIC - **The RUNME notebook** is the entry point of your accelerator. It creates the job and clusters your user will use to run the notebooks, acting as the definition of the integration test for this accelerator. All published solution accelerator run nightly integration tests
# MAGIC - **Util and configuration notebooks** can be stored `./util` and `./config` directories.  Example util notebooks for common tasks such as **preparing source data** and **centralizing configuration** are available in this repo and they are reused in almost every accelerator. You can save time by modifying and reusing these standard components.
# MAGIC - **Dashboards** can be saved in `./dashboard` directory and created in the `RUNME` notebook. See an example in the `RUNME` notebook in this repository. The dashboard import feature is in private preview and enabled on the [e2-demo-field-eng workspace](https://e2-demo-field-eng.cloud.databricks.com/?o=1444828305810485).
# MAGIC - **Images and other arbitrary files** can be stored in directories if they are not large (less than 1 mb). Imagines can be embedded via Github url once the repository is made public. See the images throughout this notebook for examples). 

# COMMAND ----------

# MAGIC %md 
# MAGIC ## Standardization: Before Reviewing with Technical Directors and other Collaborators
# MAGIC 
# MAGIC ❓ Have you created your own branch and pushed the code into your own branch?
# MAGIC 
# MAGIC ❓ Have you tested the code end-to-end? 
# MAGIC   * Set up the multi-task job in `RUNME` by modifying the sample job json - the job defines the workflow you intend the user to run in their own workspace
# MAGIC 
# MAGIC ❓ Have you created a [**pull request**](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) and tagged the reviewers?
# MAGIC   * Create a [**pull request**](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) from your branch into main. The creation of pull request triggers integration tests in multiple workspaces. [Example](https://github.com/databricks-industry-solutions/media-mix-modeling/actions)
# MAGIC   
# MAGIC ❓ Have you resolved all integration test errors? If you have issues seeing integration run histories for debugging, slack [@nicole.lu](https://databricks.enterprise.slack.com/team/jingting_lu) for help.

# COMMAND ----------

# MAGIC %md 
# MAGIC ## Publication: Before the Content is Made Publically Visible
# MAGIC 
# MAGIC Accelerators must be reviewed with the sponsoring Technical Director and 1 other technical SME. The SME can be a lead of the SME groups (ML-SME, delta-perf-sme) or a vertical lead SA.
# MAGIC 
# MAGIC ❓ Have you resolved all integration test errors? 
# MAGIC 
# MAGIC ❓ Does your accelerator have in-depth discussion with at least one focus: **business use case**, **technical pattern** or both
# MAGIC 
# MAGIC ❓ Does the notebook(s) explain the business use case and the technical pattern via sufficient Markdowns?

# COMMAND ----------

# MAGIC %md 
# MAGIC  If your answers are yes to all the above ... 
# MAGIC ## 🍻 Congratulations! You have successfully published a solution accelerator. 
# MAGIC 
# MAGIC Your thought leadership  
# MAGIC * Is visible on the Databricks [website](https://www.databricks.com/solutions/accelerators)
# MAGIC * May be showcased on our Marketplace
# MAGIC * May be used in training material
# MAGIC * Maybe implemented by our Professional Services, Cloud Partners, SIs and have many more channels of influence.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Maintenance, Feedback and Continued Improvement
# MAGIC ❗ If you know of a customer who benefited from an accelerator, you or the account team should fill out the customer use capture form [here](https://docs.google.com/forms/d/1Seo5dBNYsLEK7QgZ1tzPvuA9rxXxr1Sh_2cwu9hM9gM/edit)
# MAGIC 
# MAGIC ❗ You can track which Customer Accounts imported your accelerator if you have [logfood](https://adb-2548836972759138.18.azuredatabricks.net/login.html?o=2548836972759138&next_url=%2Fsql%2Fdashboards%2F81967c71-528d-4a92-97c7-211980470261%3Fo%3D2548836972759138) access. 
# MAGIC 
# MAGIC ❗ [@nicole.lu](https://databricks.enterprise.slack.com/team/jingting_lu) may reach out for help if some hard-to-resolve bugs arose from nightly testing
# MAGIC 
# MAGIC ❗ Users may open issues to ask questions about the accelerator. Users may also contribute to solution accelerators as long as they accept our Contributing License Agreement. We have an automated CLA process in place! All they need to do is accepting the CLA while making the pull request
