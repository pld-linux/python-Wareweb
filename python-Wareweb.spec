Summary:	WSGI web framework based on Webware/WebKit's servlet model
Summary(pl.UTF-8):	Szkielet aplikacji WWW WSGI oparty na modelu serwletowym Webware/WebKit
Name:		python-Wareweb
Version:	0.1
Release:	1
Group:		Development/Languages/Python
License:	X11/MIT
Source0:	http://cheeseshop.python.org/packages/source/W/Wareweb/Wareweb-%{version}.tar.gz
# Source0-md5:	a676d67f30e146360e90c0d8c615b6de
URL:		http://pythonpaste.org/
BuildRequires:	python-devel
%pyrequires_eq  python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a servlet-style web framework, similar to Webware, but both 
more minimal and more convenient.

%description -l pl.UTF-8
Jest to narzędzie do tworzenia serwletów (aplikacji) WSGI, podobne
do Webware, jednak prostsze i bardziej wygodne.

%prep
%setup -q -n Wareweb-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install \
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
