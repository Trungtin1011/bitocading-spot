# ArgoCD Project on EKS Cluster

**Repo Owner**: trungtin

<br>

## Repository structure

1. [helm-only](./helm-only)
ArgoCD deployment with `Helm` native config management tool only.

The folder contains 3 subfolders. Subfolder `root` contains the application root app and the initial argocd application.

Subfolder `apps` contains the application definition for each deployed application (`Application` resource or `ApplicationSet` resource).

Subfolder `manifests` contains the main helm chart for deploying each application.

<br>

2. [kustomize-enable-helm](./kustomize-enable-helm)
ArgoCD deployment with Config Management Plugin (CPM) `kustomize --enable-helm`.

The folder contains 4 subfolders. Subfolder `root` contains the application root app and the initial argocd application.

Subfolder `apps` contains the application definition for each deployed application (`Application` resource or `ApplicationSet` resource).

Subfolder `manifests` contains the main helm chart for deploying each application.

Subfolder `imgs` contains screenshots for references.

<br>

## Screenshots and documentation

### Deployment screenshots

**Applications overviews (List view)**
![listview](kustomize-enable-helm/imgs/apps-list-view.png)

<br>

**Root-app details**
![rootapp](kustomize-enable-helm/imgs/apps-tree-view.png)

<br>

**Ingress application details (Manifest and Network flows)**
![manifest](kustomize-enable-helm/imgs/app-details-ingress.png)

<br>

![network](kustomize-enable-helm/imgs/app-flows-ingress.png)

<br>

**ArgoCD application network flow**
![argocd](kustomize-enable-helm/imgs/app-flows-argocd.png)

<br>

**ApplicationSet will have a slightly difference on the Tree**
![appset](kustomize-enable-helm/imgs/apps-tree-view-appset.png)

<br>

### Reference documentation
1. [ArgoCD Architecture](https://argo-cd.readthedocs.io/en/stable/developer-guide/architecture/components/)
2. [Setup ArgoCD with Helm](https://www.arthurkoziel.com/setting-up-argocd-with-helm/)
3. [Render Helm chart with Kustomize](https://pet2cattle.com/2023/01/kustomize-render-helm)
4. [Kustomize Enable Helm](https://codefresh.io/blog/using-argo-cds-new-config-management-plugins-to-build-kustomize-helm-and-more/)
