# ExpenseManager

## Project Overview
**ExpenseManager** is a web application designed to manage employee expense claims efficiently. The app enables employees to submit their expenses, which are then reviewed and approved by managers. The system includes role-based permissions and an approval workflow to ensure the smooth processing of claims.

## Features
- **Expense Claim Management**:
  - Created an "Expense Claim" DocType with fields for:
    - **Employee Name**
    - **Expense Type** (Travel, Meals, etc.)
    - **Date**
    - **Amount**
  
- **Approval Workflow**:
  - **Employee Submission**: Employees submit their expense claims (Status: "Submitted").
  - **Manager Review**: Managers review claims (Status: "Under Review").
  - **Final Approval/Reject**: The manager either approves or rejects the claim, updating the status to "Approved" or "Rejected".

- **Role-Based Permissions**:
  - **Employees** can submit claims.
  - **Managers** can approve or reject claims.

## Installation Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/Kusum23-sinha/Expense-Manager.git


