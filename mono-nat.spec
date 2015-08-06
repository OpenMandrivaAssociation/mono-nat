%define name mono-nat
%define version 1.1.0
%define release 3

Summary: Network Address Translation library for Mono
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.gz
Source100: %{name}.rpmlintrc
License: MIT
Group: System/Libraries
Url:  http://projects.qnetp.net/news/show/8
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: mono-devel
BuildArch: noarch

%description
This is a .NET Library for automatic network address translation.

%prep
%setup -q

%build
./configure --prefix=%_prefix
make

%install
rm -rf %{buildroot}
%makeinstall_std linuxpkgconfigdir=%_datadir/pkgconfig

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%_prefix/lib/mono-nat
%_datadir/pkgconfig/mono.nat.pc



%changelog
* Thu Mar 08 2012 Götz Waschk <waschk@mandriva.org> 1.1.0-2mdv2012.0
+ Revision: 783402
- yearly rebuild

* Mon Mar 07 2011 Götz Waschk <waschk@mandriva.org> 1.1.0-1
+ Revision: 642410
- new version
- update URL

* Tue Jun 30 2009 Götz Waschk <waschk@mandriva.org> 1.0.2-1mdv2011.0
+ Revision: 390907
- new version

* Fri Feb 20 2009 Götz Waschk <waschk@mandriva.org> 1.0-1mdv2009.1
+ Revision: 343228
- import mono-nat


