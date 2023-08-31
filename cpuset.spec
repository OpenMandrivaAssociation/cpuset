Summary:	Allows manipulation of cpusets on system and provides higher level functions
Name:		cpuset
Version:	1.6.1
Release:	1
License:	GPLv2
Group:		System/Kernel and hardware
Url:		http://code.google.com/p/cpuset
Source0:	https://github.com/lpechacek/cpuset/archive/v%{version}.tar.gz
BuildRequires:	pkgconfig(python3)
BuildArch:	noarch

%description
Cpuset is a Python application to make using the cpusets facilities in the
Linux kernel easier.  The actual included command is called cset and it allows
manipulation of cpusets on the system and provides higher level functions such
as implementation and control of a basic CPU shielding setup.

%prep
%setup -q

%build
CFLAGS="%{optflags}" \
python setup.py build
#make doc  ->not yet, asciidoc is missing...

%install
# Install binaries, but do not install docs via setup.py
python setup.py \
	install --root=%{buildroot} \
	--prefix=%{_prefix} \
	--install-data=/eraseme
rm -rf %{buildroot}/eraseme

# Install documentation
mkdir -p %{buildroot}/%{_defaultdocdir}/cpuset
cp NEWS README INSTALL AUTHORS COPYING cset.init.d %{buildroot}/%{_defaultdocdir}/cpuset/
mkdir -p %{buildroot}/%{_mandir}/man1
cd doc
cp *.1 %{buildroot}/%{_mandir}/man1
cp *.txt %{buildroot}/%{_defaultdocdir}/cpuset/
mkdir %{buildroot}/%{_defaultdocdir}/cpuset/html
cp *.html %{buildroot}/%{_defaultdocdir}/cpuset/html/

%files
%{_bindir}/cset
%{python_sitelib}/*
%{_mandir}/man1/*
%{_defaultdocdir}/*

