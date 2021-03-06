Summary:	WSGI web framework based on Webware/WebKit's servlet model
Summary(pl.UTF-8):	Szkielet aplikacji WWW WSGI oparty na modelu serwletowym Webware/WebKit
Name:		python-Wareweb
Version:	0.3
Release:	5
License:	X11/MIT
Group:		Development/Languages/Python
Source0:	http://cheeseshop.python.org/packages/source/W/Wareweb/Wareweb-%{version}.tar.gz
# Source0-md5:	2f12a625120cb199f0f86d9449829551
URL:		http://pythonpaste.org/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
%pyrequires_eq  python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a servlet-style web framework, similar to Webware, but both
more minimal and more convenient.

%description -l pl.UTF-8
Jest to narzędzie do tworzenia serwletów (aplikacji) WSGI, podobne do
Webware, jednak prostsze i bardziej wygodne.

%prep
%setup -q -n Wareweb-%{version}

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install \
	--single-version-externally-managed \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc docs/
%{py_sitescriptdir}/wareweb
%{py_sitescriptdir}/Wareweb*
